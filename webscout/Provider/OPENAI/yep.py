import time
import uuid
import cloudscraper  # Import cloudscraper
import json
from typing import List, Dict, Optional, Union, Generator, Any

# Import base classes and utility structures
from .base import OpenAICompatibleProvider, BaseChat, BaseCompletions
from .utils import (
    ChatCompletionChunk, ChatCompletion, Choice, ChoiceDelta,
    ChatCompletionMessage, CompletionUsage, get_system_prompt  # Import get_system_prompt
)

# Attempt to import LitAgent, fallback if not available
try:
    from webscout.litagent import LitAgent
except ImportError:
    # Define a dummy LitAgent if webscout is not installed or accessible
    class LitAgent:
        def generate_fingerprint(self, browser: str = "chrome") -> Dict[str, Any]:
            print("Warning: LitAgent not found. Using default minimal headers.")
            return {
                "accept": "*/*",
                "accept_language": "en-US,en;q=0.9",
                "platform": "Windows",
                "sec_ch_ua": '"Not/A)Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
                "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
                "browser_type": browser,
            }

# --- YEPCHAT Client ---

# ANSI escape codes for formatting
BOLD = "\033[1m"
RED = "\033[91m"
RESET = "\033[0m"

class Completions(BaseCompletions):
    def __init__(self, client: 'YEPCHAT'):
        self._client = client

    def create(
        self,
        *,
        model: str,
        messages: List[Dict[str, str]],
        max_tokens: Optional[int] = 1280,
        stream: bool = False,
        temperature: Optional[float] = 0.6,
        top_p: Optional[float] = 0.7,
        system_prompt: Optional[str] = None,  # Added for consistency, but will be ignored
        **kwargs: Any
    ) -> Union[ChatCompletion, Generator[ChatCompletionChunk, None, None]]:
        """
        Creates a model response for the given chat conversation using YEPCHAT API.
        Mimics openai.chat.completions.create
        Note: YEPCHAT does not support system messages. They will be ignored.
        """
        if model not in self._client.AVAILABLE_MODELS:
            raise ValueError(
                f"Invalid model: {model}. Choose from: {self._client.AVAILABLE_MODELS}"
            )

        # Filter out system messages and warn the user if any are present
        filtered_messages = []
        has_system_message = False
        if get_system_prompt(messages) or system_prompt:  # Check both message list and explicit param
            has_system_message = True

        for msg in messages:
            if msg["role"] == "system":
                continue  # Skip system messages
            filtered_messages.append(msg)

        if has_system_message:
            # Print warning in bold red
            print(f"{BOLD}{RED}Warning: YEPCHAT does not support system messages, they will be ignored.{RESET}")

        # If no messages left after filtering, raise an error
        if not filtered_messages:
            raise ValueError("At least one user or assistant message is required for YEPCHAT.")

        payload = {
            "stream": stream,
            "max_tokens": max_tokens,
            "top_p": top_p,
            "temperature": temperature,
            "messages": filtered_messages,  # Use filtered messages
            "model": model,
        }

        # Add any extra kwargs to the payload
        payload.update(kwargs)

        request_id = f"chatcmpl-{uuid.uuid4()}"
        created_time = int(time.time())

        if stream:
            return self._create_stream(request_id, created_time, model, payload)
        else:
            return self._create_non_stream(request_id, created_time, model, payload)

    def _create_stream(
        self, request_id: str, created_time: int, model: str, payload: Dict[str, Any]
    ) -> Generator[ChatCompletionChunk, None, None]:
        try:
            # Use session.post from cloudscraper instance
            response = self._client.session.post(
                self._client.api_endpoint,
                headers=self._client.headers,
                cookies=self._client.cookies,
                json=payload,
                stream=True,
                timeout=self._client.timeout
            )

            if not response.ok:
                # Simplified error handling for now, add refresh logic if needed
                raise IOError(
                    f"YEPCHAT API Error: {response.status_code} {response.reason} - {response.text}"
                )

            for line in response.iter_lines(decode_unicode=True):
                if line:
                    line = line.strip()
                    if line.startswith("data: "):
                        json_str = line[6:]
                        if json_str == "[DONE]":
                            break
                        try:
                            data = json.loads(json_str)
                            choice_data = data.get('choices', [{}])[0]
                            delta_data = choice_data.get('delta', {})
                            finish_reason = choice_data.get('finish_reason')
                            content = delta_data.get('content')

                            if content is not None:  # Only yield chunks with content
                                delta = ChoiceDelta(content=content, role=delta_data.get('role', 'assistant'))
                                choice = Choice(index=0, delta=delta, finish_reason=finish_reason)
                                chunk = ChatCompletionChunk(
                                    id=request_id,
                                    choices=[choice],
                                    created=created_time,
                                    model=model,
                                )
                                yield chunk

                        except json.JSONDecodeError:
                            print(f"Warning: Could not decode JSON line: {json_str}")
                            continue

            # Yield final chunk with finish reason if not already sent
            delta = ChoiceDelta()
            choice = Choice(index=0, delta=delta, finish_reason="stop")  # Assume stop if loop finishes
            chunk = ChatCompletionChunk(
                id=request_id,
                choices=[choice],
                created=created_time,
                model=model,
            )
            yield chunk

        except cloudscraper.exceptions.CloudflareChallengeError as e:
            pass

    def _create_non_stream(
        self, request_id: str, created_time: int, model: str, payload: Dict[str, Any]
    ) -> ChatCompletion:
        full_response_content = ""
        finish_reason = "stop"  # Assume stop unless error occurs

        try:
            stream_generator = self._create_stream(request_id, created_time, model, payload)
            for chunk in stream_generator:
                if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content:
                    full_response_content += chunk.choices[0].delta.content
                if chunk.choices and chunk.choices[0].finish_reason:
                    finish_reason = chunk.choices[0].finish_reason  # Capture finish reason if provided

        except IOError as e:
            print(f"Error obtaining non-stream response from YEPCHAT: {e}")
            finish_reason = "error"

        # Construct the final ChatCompletion object
        message = ChatCompletionMessage(
            role="assistant",
            content=full_response_content
        )
        choice = Choice(
            index=0,
            message=message,
            finish_reason=finish_reason
        )
        # Usage data is not provided by this API in a standard way, set to 0
        usage = CompletionUsage(prompt_tokens=0, completion_tokens=0, total_tokens=0)

        completion = ChatCompletion(
            id=request_id,
            choices=[choice],
            created=created_time,
            model=model,
            usage=usage,
        )
        return completion

class Chat(BaseChat):
    def __init__(self, client: 'YEPCHAT'):
        self.completions = Completions(client)

class YEPCHAT(OpenAICompatibleProvider):
    """
    OpenAI-compatible client for YEPCHAT API.

    Usage:
        client = YEPCHAT()
        response = client.chat.completions.create(
            model="DeepSeek-R1-Distill-Qwen-32B",
            messages=[{"role": "user", "content": "Hello!"}]
        )
        print(response.choices[0].message.content)
    """
    AVAILABLE_MODELS = ["DeepSeek-R1-Distill-Qwen-32B", "Mixtral-8x7B-Instruct-v0.1"]

    def __init__(
        self,
        timeout: int = 30,
        browser: str = "chrome"
    ):
        """
        Initialize the YEPCHAT client.

        Args:
            timeout: Request timeout in seconds.
            browser: Browser name for LitAgent to generate User-Agent.
        """
        self.timeout = timeout
        self.api_endpoint = "https://api.yep.com/v1/chat/completions"
        self.session = cloudscraper.create_scraper()  # Use cloudscraper

        # Initialize LitAgent for user agent generation and fingerprinting
        try:
            agent = LitAgent()
            fingerprint = agent.generate_fingerprint(browser=browser)
        except Exception as e:
            print(f"Warning: Failed to generate fingerprint with LitAgent: {e}. Using fallback.")
            # Fallback fingerprint data
            fingerprint = {
                "accept": "*/*",
                "accept_language": "en-US,en;q=0.9",
                "sec_ch_ua": '"Not/A)Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
                "platform": "Windows",
                "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
            }

        # Initialize headers using the fingerprint
        self.headers = {
            "Accept": fingerprint["accept"],
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": fingerprint["accept_language"],
            "Content-Type": "application/json; charset=utf-8",
            "DNT": "1",
            "Origin": "https://yep.com",
            "Referer": "https://yep.com/",
            "Sec-CH-UA": fingerprint["sec_ch_ua"] or '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
            "Sec-CH-UA-Mobile": "?0",
            "Sec-CH-UA-Platform": f'"{fingerprint["platform"]}"',
            "User-Agent": fingerprint["user_agent"],
        }
        self.session.headers.update(self.headers)

        # Generate cookies (consider if these need refreshing or specific values)
        self.cookies = {"__Host-session": uuid.uuid4().hex, '__cf_bm': uuid.uuid4().hex}

        # Initialize the chat interface
        self.chat = Chat(self)

    @property
    def models(self):
        class _ModelList:
            def list(inner_self):
                return YEPCHAT.AVAILABLE_MODELS
        return _ModelList()

    def convert_model_name(self, model: str) -> str:
        """
        Ensures the model name is valid for YEPCHAT.
        Returns the validated model name or raises an error if invalid.
        """
        if model in self.AVAILABLE_MODELS:
            return model
        else:
            # Raise error instead of defaulting, as model is mandatory in create()
            raise ValueError(f"Model '{model}' not supported by YEPCHAT. Available: {self.AVAILABLE_MODELS}")

# Example usage (optional, for testing)
if __name__ == '__main__':
    print("Testing YEPCHAT OpenAI-Compatible Client...")

    # Test Non-Streaming
    try:
        print("\n--- Non-Streaming Test (DeepSeek) ---")
        client = YEPCHAT()
        response = client.chat.completions.create(
            model="DeepSeek-R1-Distill-Qwen-32B",
            messages=[
                {"role": "user", "content": "Say 'Hello World'"}
            ],
            stream=False
        )
        print("Response:", response.choices[0].message.content)
        print("Usage:", response.usage)  # Will show 0 tokens
    except Exception as e:
        print(f"Non-Streaming Test Failed: {e}")

    # Test Streaming
    try:
        print("\n--- Streaming Test (Mixtral) ---")
        client_stream = YEPCHAT()
        stream = client_stream.chat.completions.create(
            model="Mixtral-8x7B-Instruct-v0.1",
            messages=[
                {"role": "user", "content": "Write a short sentence about AI."}
            ],
            stream=True
        )
        print("Streaming Response:")
        for chunk in stream:
            content = chunk.choices[0].delta.content
            if content:
                print(content, end="", flush=True)
        print()  # Add a newline at the end

    except Exception as e:
        print(f"Streaming Test Failed: {e}")
