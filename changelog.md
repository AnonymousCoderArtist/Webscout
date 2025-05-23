# WebScout Changelog


## Version 8.2.8 (May 2025)

### 2025-05-18
- ✨ **Feature:** Added NEMOTRON as an OpenAI-compatible provider.
- 📝 **Documentation:** Updated documentation and imports for NEMOTRON provider.
- 🛠️ **Improve:** Refined conversation validation logic for improved streaming support and role normalization, enhancing reliability.
- 🔨 **Refactor:** Simplified TypefullyAI provider by removing excessive comments and redundant docstrings for conciseness and maintainability.
- 🔄 **Update:** Updated available model lists for relevant providers.
- 💄 **Style:** Adjusted output formatting for clearer feedback.

- ✨ **Feature:** Added new models to LLMChat provider: `llama-4-scout-17b-16e`, `mistral-small-3.1-24b`, and `gemma-3-12b-it`.
- 🔨 **Refactor:** Converted models classmethod to property with `.list()` for all OpenAI providers, improving interface consistency and model discovery.
- 🛠️ **Improve:** Enhanced Meta provider response handling to always yield the latest message.
- 🐛 **Fix:** Improved error handling during conversation loading.
- 🔧 **Feature:** Introduced new labeler configuration for GitHub Actions.
- ✨ **Feature:** Implemented Flowith provider with streaming support for Flowith API.
- ✨ **Feature:** Created Cloudflare provider for OpenAI-compatible API interactions.
- ✨ **Feature:** Developed ChatSandbox provider for OpenAI-compatible chat interactions.
- 🪵 **Improve:** Enhanced Flowith provider with detailed request and response logging.
- ✨ **Feature:** Added Samurai provider for custom API interactions with improved error handling and streaming support.
- ✨ **Feature:** Added OpenAI-compatible API server for unified model serving and integration.
- 📝 **Documentation:** Updated documentation to reflect new providers, API server, and usage examples.
- 🔄 **Update:** Updated model list for TextPollinationsAI provider: added `openai-roblox` and removed `llama-vision`.
- 🐛 **Fix:** Resolved issue in `LambdaChat` provider that caused duplicate responses by removing redundant `finalAnswer` handling.
- ✨ **Feature:** Added LMArena provider in webscout
- ✨ **Feature:** Added Sthir provider with text-to-speech functionality.
- 🔄 **Update:** Updated SpeechMa provider voices.
- 🛠️ **Fix:** Fixed and expands model support and refines BlackboxAI integration. Extensively updates model selection with new agent and OpenRouter models, improves model aliasing and user selection logic, and implements dynamic session and request generation to better emulate client behavior. Enhances error handling, adds vision model support, and refreshes API payloads and headers for improved compatibility and maintainability.


## Version 8.2.7 (May 2025)

### 2025-05-10

- 🔨 **Refactor:** Migrated project configuration from `setup.py` to `pyproject.toml` for modern Python packaging standards. (#OEvortex)
- 🐛 **Fix:** Resolved CLI entrypoint issue by correcting the function reference in package configuration. (#OEvortex)
- 🗑️ **Remove:** Removed legacy `setup.py` file after complete migration to `pyproject.toml`. (#OEvortex)
- ✨ **Improve:** Enhanced AUTO provider to automatically exclude providers requiring authentication tokens or cookies. (#OEvortex)
- 🔧 **Feature:** Added option to print successful provider name in AUTO provider for better debugging. (#OEvortex)
- ✨ **Feature:** Implemented OpenAI-compatible interface for TypefullyAI provider with streaming support and standardized prompt formatting. (#OEvortex)
- 🔄 **Update:** Refreshed model list for TextPollinationsAI provider with latest available models. (#OEvortex)
- 🔄 **Update:** Updates model mapping in SciraChat providers
- 🐛 **Fix:** Enhanced shell command handling with `!` prefix in autocoder: (#OEvortex)
  - Modified `_extract_code_blocks` to properly detect shell commands in code blocks
  - Added support for shell commands in triple backticks without language tag
  - Implemented Jupyter-style UI for shell command execution and output display
  - Fixed issue with `main` method not properly handling shell commands
  - Added support for multiple shell commands in a single code block
  - Enhanced error handling and display for shell commands
- 🔧 **Feature:** Added limit parameter to trending video methods and updated model mapping: (#OEvortex)
  - Introduced optional limit parameter to all trending video retrieval methods
  - Allows trending video results to be capped directly within method calls
  - Updated AI model mapping to include support for an additional model
  - Improved provider flexibility with enhanced model support

## Version 8.2.6 (May 2025)

### 2025-05-05

- ✨ **Feature:** Added new model support for `GizAI` provider with enhanced API error handling. (#OEvortex)
- 🔨 **Refactor:** Optimized response streaming in `ChatSandbox` and `TypliAI` providers for better performance. (#OEvortex)
- 📝 **Documentation:** Updated README with new examples for GGUF converter usage. (#OEvortex)

### 2025-05-04

- ✨ **Feature:** Implemented batch processing capability in `MultiChatAI` provider. (#OEvortex)
- 🔧 **Change:** Updated default timeout values across all providers for better reliability. (#OEvortex)
- 🐛 **Fix:** Resolved memory leak issue in `TwoAI` streaming implementation. (#OEvortex)

### 2025-05-03

- ✨ **Feature:** Added experimental support for `SonusAI` voice synthesis models. (#OEvortex)
- 🔨 **Refactor:** Cleaned up import statements in `ElectronHub` for better code organization. (#OEvortex)
- 📝 **Documentation:** Added troubleshooting section for GGUF converter in README. (#OEvortex)

## Version 8.2.5 (May 2025)

### 2025-05-02

- 🔧 **Change:** Removed `inferno` folder and made it a standalone package: `inferno-llm` (available via `pip install inferno-llm`). (#OEvortex)
- 🔧 **Change:** Removed `webscout/Local` module as it's now part of the standalone Inferno package. (#OEvortex)
- 📝 **Documentation:** Updated README to reflect Inferno is now a standalone package with links to GitHub and PyPI repositories. (#OEvortex)
- ✨ **Feature:** Implemented `GizAI` provider for API interaction and enhanced response handling. (#OEvortex)
- 📝 **Documentation:** Added detailed documentation for GGUF converter with comprehensive usage examples and features. (#OEvortex)
- ✨ **Feature:** Implemented Google and Yep search commands in CLI with configurable options for region, safesearch, and result filtering. (#OEvortex)
- 🔨 **Refactor:** Cleaned up message validation logic in conversation module for improved reliability. (#OEvortex)

### 2025-05-01

- ✨ **Feature:** Added `ChatSandbox` and `TypliAI` providers with enhanced API interaction capabilities. (#OEvortex)
- 📝 **Documentation:** Updated README to add `MultiChatAI`, `AI4Chat`, and `MCPCore` to available providers list. (#OEvortex)
- ✨ **Feature:** Updated `TwoAI` API endpoint and enhanced streaming response handling for better performance. (#OEvortex)
- 🔨 **Refactor:** Cleaned up import statements in `ElectronHub` and `Glider` files for improved code readability. (#OEvortex)
- 🔨 **Refactor:** Integrated `sanitize_stream` for improved response handling across multiple providers: (#OEvortex)
  - Added to `MultiChatAI` for processing raw responses
  - Updated `SciraAI` for both streaming and non-streaming responses with error handling
  - Implemented in `SCNet` for JSON extraction from streaming data
  - Enhanced `SearchChatAI` for efficient data processing
  - Integrated in `SonusAI` for better content extraction from responses
  - Refactored `Toolbaz` to use `sanitize_stream` for tag removal in streaming text
  - Updated `TurboSeek` for JSON object extraction
  - Implemented in `TypefullyAI` for improved content extraction from streaming responses
  - Enhanced `TypeGPT` for both streaming and non-streaming responses
  - Integrated in `UncovrAI` for better handling of streaming and non-streaming data

## Version 8.2.4 (May 2025)

### 2025-05-01

- ✨ **Feature:** Enhanced `AIutel.py` chunk processing with byte stream decoding and integrated `sanitize_stream` across multiple providers (`yep.py`, `x0gpt.py`, `WiseCat.py`, `WritingMate.py`, `Writecream.py`, `HeckAI.py`) for improved data handling and cleaner code. (#OEvortex)

### 2025-04-30

- ✨ **Feature:** Implemented `MCPCore` API client (`Provider/OPENAI/mcpcore.py`) with model support and cookie handling. (#OEvortex)

### 2025-04-29

- ✨ **Feature:** Updated available models list for `HeckAI` provider. (#OEvortex)
- ✨ **Feature:** Updated available models list for `DeepInfra` and `ElectronHub` providers, adding dynamic model fetching. (#OEvortex)

### 2025-04-27

- ✨ **Feature:** Implemented `Groq` client (`Provider/OPENAI/groq.py`) for chat completions, switching API usage and updating model handling. (#OEvortex)
- ✨ **Feature:** Implemented model fetching from Groq API, updated available models, and switched to `curl_cffi` for HTTP requests in `Groq` provider (`Provider/Groq.py`). (#OEvortex)
- 🔨 **Refactor:** Refactored `ChatGPTClone` to use `curl_cffi`, removed `ChatGPTES`, added `AI4Chat`, enhanced error handling, and updated headers/session initialization across providers. (#OEvortex)

### 2025-04-25

- ✨ **Feature:** Added GGUF RAM estimation utilities and `MultiChatAI` provider implementation with support for multiple endpoints and streaming. (#OEvortex)

### 2025-04-23

- 🔨 **Refactor:** Replaced `primp` library with `curl_cffi` for HTTP requests across the `webscout` package. (#OEvortex)

## Version 8.2.3 (23 April 2025)

### 2025-04-23

- ✨ **Feature:** Implemented base TTS provider with audio saving and streaming functionality (#OEvortex)
  - Added foundational TTS provider class
  - Enabled audio file saving and streaming support

### 2025-04-22

- ✨ **Feature:** Updated available models in Toolbaz provider (#OEvortex)

### 2025-04-21

- 🗑️ **Remove:** Removed unfinished E2B API and Emailnator implementations (now completed) (#OEvortex)

## Version 8.2.2 (20 April 2024)

### 2024-04-20

- ✨ **Feature:** Added new models to E2B provider (#OEvortex)
  - Added support for o4-mini, gpt-4o-mini, gpt-4-turbo models
  - Added support for Qwen2.5-Coder-32B-Instruct model
  - Added support for DeepSeek R1 model

- 🔧 **Fix:** Updated Dependabot reviewer username to OEvortex (#OEvortex)

- 🔧 **Fix:** Fixed issues in the inferno CLI module (#OEvortex)

### 2024-04-19

- ✨ **Feature:** Implemented Emailnator provider for TempMail and updated provider list (#OEvortex)
  - Added new temporary email provider
  - Updated provider listings to include the new service

## Version 8.2.1 (19 April 2024)

### 2024-04-19

- ✨ **Feature:** Added E2B provider to OPENAI directory (#OEvortex)
  - Implemented OpenAI-compatible interface for E2B API
  - Added support for various models including claude-3.5-sonnet
  - ~~Enabled both streaming and non-streaming completions~~
  - Included comprehensive error handling and response formatting

## Version 8.2 (18 April 2024)

### 2024-04-18

- ✨ **Feature:** Implemented webscout.Local module with command-line interface (#OEvortex)
  - Added cli.py for managing models, including commands to serve, pull, list, remove, and run models
  - Integrated model management and loading functionalities
  - Enhanced user interaction with rich console outputs and prompts

- ✨ **Feature:** Added configuration management for webscout.Local (#OEvortex)
  - Introduced config.py to handle application configuration
  - Implemented loading, saving, and accessing configuration values
  - Default configurations for models directory, API host, and port

- ✨ **Feature:** Created LLM interface for local model integration (#OEvortex)
  - Developed llm.py to interface with llama-cpp-python for model loading and completion generation
  - Added methods for creating completions and chat responses

- ✨ **Feature:** Implemented model management functionalities (#OEvortex)
  - Created model_manager.py for downloading, listing, and removing models
  - Integrated Hugging Face Hub for model downloads and file management

- ✨ **Feature:** Implemented OpenAI-compatible API server (#OEvortex)
  - Added server.py to create an OpenAI-compatible API using FastAPI
  - Implemented endpoints for model listing and chat/completion requests

- ✨ **Feature:** Added utility functions for webscout.Local (#OEvortex)
  - Introduced utils.py for various utility functions including duration parsing and image encoding/decoding

- ✨ **Feature:** Added Perplexity search provider and updated README with examples (#OEvortex)

- ✨ **Feature:** Added XAI model configuration and updated available models in ExaChat (#OEvortex)

- ✨ **Feature:** Added WritingMate provider and updated cleanup script to remove .pytest_cache (#OEvortex)

- ✨ **Feature:** Updated available models in SciraAI and SciraChat (#OEvortex)

- ✨ **Feature:** Integrated TextPollinations API and updated related models (#OEvortex)

### 2024-04-17

- ✨ **Feature:** Switched from OPKFC to ChatGPT and updated model to auto (#OEvortex)

- 🧹 **Cleanup:** Removed all compiled Python files (.pyc) from the __pycache__ directories (#OEvortex)
  - Ensured a clean build environment and prevented potential issues with stale bytecode

- ✨ **Feature:** Added OPKFC as new provider (#OEvortex)

- ✨ **Feature:** Added scira-o4-mini model to available models in SciraChat and SciraAI (#OEvortex)

- ✨ **Feature:** Implemented UncovrAI API integration and updated related files (#OEvortex)

### 2024-04-16

- ✨ **Feature:** Updated endpoints and added new models for ExaChat, GithubChat, Glider, and YouChat (#OEvortex)

### 2024-04-15

- ✨ **Feature:** Added Toolbaz and SCNet API implementations (#OEvortex)
  - Updated __init__.py for new providers

- ✨ **Feature:** Implemented Writecream API integration and updated client initialization (#OEvortex)

- ✨ **Feature:** Added StandardInputAI and E2B API implementations (#OEvortex)
  - Implemented StandardInputAI class for interacting with the Standard Input chat API
  - Added E2B class for encapsulating the E2B API, supporting various models
  - Included methods for building request bodies, merging user messages, and generating system prompts
  - Enhanced error handling and response parsing for API requests

### 2024-04-14

- ✨ **Feature:** Enhanced setup.py with additional classifiers and keywords (#OEvortex)

## Version 8.1 (14 April 2024)

### 2024-04-14

- ✨ **Feature:** Added OpenAI-compatible interfaces for multiple providers, enabling standardized API access (#OEvortex)
  - Implemented OpenAI-compatible interfaces for DeepInfra, Glider, ChatGPTClone, X0GPT, WiseCat, Venice, ExaAI, TypeGPT, SciraChat, LLMChatCo, FreeAIChat, and YEPCHAT
  - Added comprehensive documentation with usage examples for all OpenAI-compatible providers
  - Created standardized response formats matching OpenAI's structure for better compatibility

- 🔧 **Fix:** Resolved minor bugs in native compatibility implementations (#OEvortex)
  - Enhanced error handling and response processing across multiple providers
  - Improved model validation and selection logic
  - Standardized timeout handling for better reliability

- 📝 **Documentation:** Added detailed README for OpenAI-compatible providers with examples and model listings (#OEvortex)
  - Created comprehensive provider-specific documentation
  - Added code examples for both streaming and non-streaming usage
  - Updated main README with information about dual compatibility options

## Version 8.0 (13 April 2024)

### 2024-04-13

- 🔼 **Version:** Updated version to 8.0 (#OEvortex)
- ✨ **Feature:** Added SciraAI search provider with streaming support, multiple models, and DeepSearch capabilities (#OEvortex)
- ✨ **Feature:** Introduced 'gemini-2.5-pro' model to GitHub Chat for advanced interactions (#OEvortex)
- ✨ **Feature:** Enhanced DeepInfra with configurable system prompts and updated model availability (#OEvortex)
- ✨ **Feature:** Improved model configurations for Hika, ExaAI, and Netwrck providers (#OEvortex)
- ✨ **Feature:** Added support for new providers: OpenGPT, WebpilotAI, Hika, ExaAI, LLMChatCo, and TypefullyAI (#OEvortex)
- 🗑️ **Remove:** Removed non-functional models from DeepInfra for a cleaner experience (#OEvortex)
- ✨ **Feature:** Enhanced video metadata extraction with additional properties for better insights in YTToolkit (#OEvortex)
- ✨ **Feature:** Added retry logic and Turnstile token handling to improve AI chat functionality (#OEvortex)
- 🔨 **Refactor:** Refactored URL handling and error management for more reliable operations (#OEvortex)
- 🔨 **Refactor:** Streamlined provider configurations and removed deprecated entries (#OEvortex)

## Version 7.9 (April 2024)

### 2024-04-09

- 🔼 **Version:** Updated version to 7.9 (#OEvortex)
- 🗑️ **Remove:** Removed Editee provider and updated imports (#OEvortex)
- ✨ **Feature:** Updated ElectronHub AVAILABLE_MODELS with new AI model entries (#OEvortex)
- ✨ **Feature:** Added Llama 4 Scout and Llama 4 Maverick to FreeAIChat AVAILABLE_MODELS (#OEvortex)
- ✨ **Feature:** Updated Gemini model aliases and removed deprecated entries (#OEvortex)

### 2025-04-08

- 💄 **Style:** Standardized formatting and indentation in system context prompts for optimizers (#OEvortex)
- ✨ **Feature:** Added informative error raising if litprinter is not installed (#OEvortex)

### 2025-04-06

- ✨ **Feature:** Added "qwen25-coder-32b-instruct" to LambdaChat AVAILABLE_MODELS list (#OEvortex)
- ✨ **Feature:** Added cerebras models and updated gemini model list in ExaChat (#OEvortex)
- ✨ **Feature:** Updated UncovrAI AVAILABLE_MODELS and enhanced error handling in response parsing (#OEvortex)
- ✨ **Feature:** Updated TextPollinationsAI AVAILABLE_MODELS list with new models and improved descriptions (#OEvortex)
- ✨ **Feature:** Restored google gemma models to DeepInfra AVAILABLE_MODELS list (#OEvortex)
- ✨ **Feature:** Updated GROQ AVAILABLE_MODELS list with new models and removed commented entries (#OEvortex)
- ✨ **Feature:** Added new models to DeepInfra AVAILABLE_MODELS list (#OEvortex)

### 2025-04-05

- 🗑️ **Remove:** Removed DARKAI provider and updated imports (#OEvortex)
- ✨ **Feature:** Added new models to FreeAIChat AVAILABLE_MODELS list (#OEvortex)
- ✨ **Feature:** Implemented TempMail package for temporary email generation (#OEvortex)
- 📝 **Documentation:** Clarified fallback behavior for litprinter import (#OEvortex)
- 🔨 **Refactor:** Replaced bundled litprinter implementation with external package import (#OEvortex)
- 🐛 **Fix:** Updated import statements and removed redundant warnings for better clarity in traceback (#OEvortex)
- 📝 **Documentation:** Revamped README with enhanced introduction, features, and installation instructions (#OEvortex)
- 📝 **Documentation:** Enhanced legal notice with clearer disclaimers and updated licensing terms (#OEvortex)
- 📝 **Documentation:** Updated changelog.md with a professional and modern format for better readability and organization (#OEvortex)

## Version 7.8 (April 2024)

### 2024-04-04

- 📝 **Documentation:** Revamped README with enhanced introduction, features, and installation instructions
  - Restructured content for better readability
  - Added comprehensive feature descriptions
  - Updated code examples for all major modules
  - Improved visual presentation with badges and formatting

### 2024-04-04

- 🔄 **Merge:** Integrated latest changes from main branch (#342d751)
- 📝 **Documentation:** Enhanced LEGAL_NOTICE.md with detailed attribution and licensing terms for improved clarity (#newcommitid)
- 🛠️ **Enhancement:** Added enhanced debugging and logging functionality with lit and litprint modules (#9b5a9cb)
- 💄 **Style:** Improved README banner presentation (#6bae2d6)

### 2024-04-03

- ✏️ **Rename:** Changed rawdog.py to autocoder.py (#529f514)
- 📝 **Documentation:** Made intro content shorter and more concise (#8bb7b81, #66e6e8c)
- 🔧 **Update:** Enhanced conversation.py prompting system (#6401a8f)
- ⚙️ **Feature:** Enhanced YEPCHAT provider with tool calling functionality and updated Conversation class to support tool management (#27c8370)
  - Added example usage for weather tool in new script

### 2024-04-02

- 🔨 **Refactor:** Updated imports to use 'litagent' module for LitAgent across multiple provider files (#51505ee)
- 🔼 **Version:** Bumped version to 7.8 in version.py (#f04d3c3)
- 🏷️ **Rename:** Changed GoogleS to GoogleSearch and enhanced search functionality (#023eb8b)
  - Improved error handling
  - Added support for text and news searches
  - Refined response parsing
  - Updated README with new usage examples

### 2024-04-01

- 🗑️ **Remove:** Deprecated autocoder_usage.py (#6d81d93)
- 🔄 **Update:** Enhanced available models in FreeAIChat and FreeAIPlayground providers (#6d81d93)
  - Added new models
  - Improved model name clarity for better user understanding
- 🔄 **Merge:** Synchronized with main repository branch (#2b90ea9)
- 🐛 **Fix:** Added "NOT WORKING" comment to oivscode.py and updated type hints (#39a97ea)
  - Included debugging print statement for response text
- ✨ **Feature:** Added thinking capabilities to autocoder (#ec676f9, #c9ea446)
- 📝 **Documentation:** Updated README to include SearchChatAI provider (#ca350e5)
  - Enhanced TTS documentation with voice selection and logging details
  - Added SearchChatAI to **init**.py for improved provider integration

### 2024-03-31

- 📝 **Documentation:** Updated README to include Aitopia provider (#0d6ff18)
  - Enhanced the list of AI services
  - Added Aitopia to **init**.py for improved provider integration
- 🔄 **Update:** Modified README to remove Devs Do Code's YouTube link and enhanced formatting (#b8c581e)
  - Added AskSteve provider to **init**.py for improved functionality

## Version 7.7 (March 2024)

### 2024-03-30

- 🔄 **Merge:** Integrated latest changes from main branch (#3162f35)
- 📝 **Documentation:** Refactored comments in `multichat.py` for consistency and clarity (#e3af93c)
  - Updated README files in `AISEARCH` and `TTI` to include new provider details and enhance formatting
  - Added `pixelmuse` to the TTI provider list for improved documentation
- 🛠️ **Enhancement:** Updated TypeGPT (#cffcb35)
- 📝 **Documentation:** Updated README and refactored type hints in AISEARCH provider files (#71b9193)
  - Added `ExaChat` to the README and `__init__.py`
  - Enhanced type clarity in `DeepFind.py`, `felo_search.py`, `genspark_search.py`, and `ISou.py` by using `Union` in method signatures, improving code readability and maintainability

### 2024-03-29

- 🔨 **Refactor:** Refactored image upload and access token retrieval in `copilot.py` (#6ab7c7c)
  - Enhanced error handling
  - Streamlined image upload process
  - Improved retrieval of access tokens and cookies from HAR files
  - Updated WebSocket message handling for better response processing
- 🔨 **Refactor:** Refactored image upload handling in `copilot.py` to improve error handling and streamline the process (#2e66e80)
  - Added checks for the presence of the `nodriver` package
  - Enhanced the retrieval of access tokens and cookies
  - Updated image upload API endpoint and improved response handling for better reliability
- 🔨 **Refactor:** Refactored type hints in `multichat.py` to use `Union` in method signatures, enhancing type clarity and improving code readability and maintainability (#a46422c)
- 🔨 **Refactor:** Refactored type hints in `typegpt.py` to enhance type clarity by incorporating `Any`, `Dict`, and `Generator`, improving code readability and maintainability (#67dd265)
- 🔨 **Refactor:** Refactored type hints in `Marcus.py` to improve type clarity by using `Union` in method signatures, enhancing code readability and maintainability (#bc5c64b)
- 🔨 **Refactor:** Refactored type hints across multiple provider files to improve type clarity by using `Union` in method signatures, enhancing code readability and maintainability (#9322f5c)
- 🔨 **Refactor:** Refactored type hints in `askmyai.py` to improve type clarity by using `Union` in method signatures, enhancing code readability and maintainability (#447ca30)
- 🔨 **Refactor:** Refactored type hints across multiple provider files to use `Union` for improved type clarity and consistency in method signatures, enhancing code readability and maintainability (#db89ef1)
- 🔨 **Refactor:** Refactored type hints in `bagoodex.py` to use `Union` for improved type clarity in method signatures, enhancing code readability and maintainability (#2f26f8d)
- 🔨 **Refactor:** Refactored type hints in `Llama3.py` to improve type clarity by using `Union` in method signatures, enhancing code readability and maintainability (#e3c6196)
- 🔨 **Refactor:** Refactored type hints across multiple provider files to use `Union` for improved type clarity and consistency in method signatures, enhancing code readability and maintainability (#df142e2)
- 🔨 **Refactor:** Refactored type hints in `Llama.py` to use `Union` for improved type clarity in method signatures, enhancing code readability and maintainability (#23597fe)
- 🔨 **Refactor:** Refactored type hints in `AIutel.py` to use `Union` for improved type clarity in the `sanitize_stream` function, enhancing code readability and maintainability (#e0b817d)
- 🔨 **Refactor:** Refactored type hints in `tempid.py` to use `List` and `Optional` for improved type clarity and consistency in method signatures, enhancing code readability and maintainability (#09c7bdd)
- 🔨 **Refactor:** Refactored type hints in `tempid.py` to use `Optional` for nullable fields, enhancing type clarity and consistency across the `MessageResponseModel` class (#c60d832)
- 🔨 **Refactor:** Enhanced type hints in `webscout/utils.py` by adding `Union` to improve type clarity and support for multiple data types (#615062d)
- 🔄 **Update:** Updated README.md to include `VercelAI` in the list of providers (#ac45518)
  - Modified `setup.py` to require Python 3.9 or higher
  - Refactored type hints in `webscout/utils.py` for improved clarity
  - Enhanced multiple provider classes by updating response handling and adding new models in `Venice.py`
  - Cleaned up imports and streamlined code in `QwenLM.py`, `uncovr.py`, and `WiseCat.py` for better maintainability

### 2025-03-28

- 📝 **Documentation:** Updated README.md files across multiple TTI providers to improve clarity and formatting (#cc0df4b)
  - Added new sections and examples
  - Ensured consistent spacing
  - Enhanced error handling descriptions
  - Notable changes include the addition of features and installation instructions for AiForce and Nexra, as well as optimizations in Piclumen and Talkai documentation
- 📝 **Documentation:** Enhanced `README.md` in the TTI provider to include the new `ImgSys` provider (#cd1037f)
  - Offers multi-provider image generation with error handling and async support

### 2025-03-28

- 🔨 **Refactor:** Refactored `Gemini.py` to remove logging functionality and streamline model initialization (#f97d30d)
  - Updated model aliases to include `2.5-exp-advanced`
  - Adjusted type hints for clarity
  - Removed unnecessary comments and logging code to enhance maintainability
- 🔨 **Refactor:** Refactored `Bard.py` to streamline model definitions and improve code clarity (#1bebc4f)
  - Removed unnecessary line breaks in the `UPLOAD` header
  - Added new model `G_2_5_EXP_ADVANCED`
  - Marked several models as deprecated with comments for future removal
  - Updated type hints in the `from_name` method for consistency

### 2024-03-25

- 🗑️ **Remove:** Deprecated `t.py` file and updated version to 7.7 in `version.py` (#7a8a4e8)
  - Refactored user agent generation in `agent.py` for improved browser handling and randomization
- 🛠️ **Enhancement:** Enhanced AutoCoder and LearnFast modules with improved error handling, execution result capture, and streamlined response processing (#ab2d335)

### 2024-03-22

- 🛠️ **Fix:** Fixed various issues (#834413b)
- 🔄 **Merge:** Integrated latest changes from main branch (#45e9adb)
- 📝 **Documentation:** Updated README and Provider modules to include new AI providers: LabyrinthAI, WebSim, LambdaChat, and ChatGPTClone (#bce699e)
  - Refactored AllenAI to streamline prompt handling
  - Removed unused logging features from multiple providers, enhancing overall code clarity and maintainability

### 2024-03-22

- ✨ **Feature:** Removed logging and added new providers (#0a6c4e9)

### 2024-03-21

- 🛠️ **Enhancement:** Enhanced GliderAI to support both standard and DeepSeek response formats (#a4244b7)
  - Improved content extraction logic for streaming text
- 📝 **Documentation:** Updated README and Provider module to include UncovrAI provider (#a225ef6)
- 🔄 **Merge:** Integrated latest changes from main branch (#8a86d9e)
- ✨ **Feature:** Added weather functionality to CLI, including a new command for retrieving weather data and a dedicated display format (#73f4006)
  - Updated README with relevant links and installation instructions
- 🔨 **Refactor:** Refactored GGUF model conversion to utilize ModelConverter class (#9156122)
  - Enhanced README examples
  - Improved type hints across the codebase
  - Updated OLLAMA provider to support tools and images in chat methods
  - Adjusted TypeGPT API endpoint for consistency

### 2024-03-21

- 🛠️ **Fix:** Fixed various issues (#c0a9488, #b1d432c)

### 2024-03-20

- 🔼 **Version:** Updated version to 7.6, removed Amigo and Bing providers from the project, and cleaned up related imports in the Provider module (#fedac8b)
  - Adjusted README to reflect current model availability
- 📝 **Documentation:** Updated license to reflect new attribution and licensing terms (#9b1d861)
  - Removed logging options from GoogleS class
  - Streamlined provider testing in multiple classes
  - Removed DiscordRocks provider
  - Enhanced model availability checks and error handling across various providers

### 2024-03-19

- 🗑️ **Remove:** Deprecated Autollama utility and related documentation from README and imports (#8a0b8de)
- 🔨 **Refactor:** Refactored GGUF model conversion process to streamline temporary directory management and encapsulate conversion logic in a helper method (#5fbefeb)
  - Improved code organization and maintained functionality for both local and upload scenarios
- 🔨 **Refactor:** Updated GGUF model converter to include type hints for imports and improve train data path assignment logic (#1c6161b)
- 🛠️ **Enhancement:** Enhanced GGUF model conversion with advanced features including imatrix quantization, model splitting, and improved hardware detection (#b12a811)
  - Updated CLI options and README generation for better user guidance

### 2024-03-17

- ✨ **Feature:** Added FastFlux image generator provider and updated README (#f9a122b)
- 🗑️ **Remove:** Deprecated AI art generation function and related imports from test.py (#c2cfe81)
- ✨ **Feature:** Added MagicStudio provider for AI image generation and updated README (#d259aee)
- 🛠️ **Fix:** Fixed various issues (#9f6c1e0, #09bbb56, #1b6ce8b)

### 2024-03-16

- 🔨 **Refactor:** Refactored imports across multiple files to streamline code and remove unused dependencies (#0024425)
- 📝 **Documentation:** Updated README with AI Search Providers and removed proxy rotation example from LitAgent documentation (#64701f2)
- 🛠️ **Enhancement:** Enhanced LitAgent with new device types, browser fingerprinting support, and updated documentation (#4744b36)
- ✨ **Feature:** Added TTS voice management functionality and updated README (#2cb678a)
- 🔨 **Refactor:** Refactored TTS provider imports, removed Voicepods provider, and updated README for new SpeechMa provider (#6ee2331)
- 📝 **Documentation:** Added weather toolkit documentation, implemented model management, and created GitHub workflows for labeling and releases (#c8721cb)

### 2024-03-14

- 🗑️ **Remove:** Deprecated pygetwindow dependency from autocoder_utiles.py (#c8f16b3)
- 🔼 **Version:** Bumped version to 7.5 (#c0226af)
- ✨ **Feature:** Added Flowith provider implementation and updated README (#82c1d38)
- 🗑️ **Remove:** Deprecated logging functionality from Cloudflare and DeepSeek providers (#671c75f)
  - Updated README to reflect changes in available models
- ✨ **Feature:** Added system prompt parameter to HuggingFaceChat initialization (#34d55c2)
- 🔄 **Merge:** Integrated latest changes from main branch (#7a0cb5a)
- 🔨 **Refactor:** Refactored DeepInfra and HuggingFaceChat providers (#9b45b6e)
  - Updated available models
  - Enhanced initialization with assistantId

### 2024-03-14

- 🔄 **Merge:** Integrated latest changes from main branch (#3c965e4, #160e127, #1f4a42a, #604d8e1)
- 🛠️ **Enhancement:** Added Dependabot configuration and workflows for automated dependency management and review (#ac8c50c)
- ✨ **Feature:** Added C4ai provider and updated README (#2da854f)
- 🔨 **Refactor:** Updated AkashGPT provider to comment out unused models and add system prompt to request payload (#5c4ad7d)
- ✨ **Feature:** Added AIArta provider with synchronous and asynchronous interfaces, and introduced AuthenticationError exception (#4ddc4a0)
- 🔨 **Refactor:** Refactored Phind and Marcus providers to standardize available models and remove logging functionality (#5338e70)
- ✨ **Feature:** Added nodriver dependency and included Copilot provider in the module exports (#b11d4a6)
- 🗑️ **Remove:** Deprecated format_prompt method from GithubChat provider (#0840b5c)
- 📝 **Documentation:** Added site removal request templates and legal notice (#1e7043d)
- ✨ **Feature:** Added GithubChat to provider list and updated README (#ae43b98)
- ✨ **Feature:** Added HuggingFaceChat to provider list and updated README (#6aed37b)

### 2024-03-09

- 🔄 **Merge:** Integrated latest changes from main branch (#e492880, #2526692, #3c9bc83)
- 🛠️ **Fix:** Fixed various issues (#e5c666c, #4784a79)
- 🔨 **Refactor:** Removed webscout.Local (#e5c666c)
- 🔼 **Version:** Bumped version to 7.4 (#4784a79)
- ✨ **Feature:** Added plus_model parameter to initialize ChatGLM API client (#88670e9)
- 🔨 **Refactor:** Removed logging functionality and updated model names in QwenLM provider (#3b05a18)
- 🛠️ **Fix:** Updated model name from "qwq-32b-preview" to "qwq-32b" in QwenLM provider (#638dcc0)

### 2024-03-08

- 🔄 **Merge:** Integrated latest changes from main branch (#edc6cea, #7ad8708, #6b46674, #ee79c12)
- 🛠️ **Enhancement:** Enhanced security and fixed text encoding for Cyrillic and other encodings (#7ad8708, #6b46674, #ee79c12)
  - Updated the list of models
  - Fixed function for_non_stream

### 2024-03-06

- ✨ **Feature:** Added PiclumenImager provider with synchronous and asynchronous support (#92f4e43)
  - Enhanced README with usage examples

### 2024-03-05

- ✨ **Feature:** Added Venice AI provider with API integration and model support (#0396126)
- ✨ **Feature:** Implemented TwoAI provider with API integration and model support (#2a892b7)
- ✨ **Feature:** Added HeckAI provider with API integration and model support (#077ae14)
- ✨ **Feature:** Added AllenAI to the list of available models in the README (#b0267c5)
- ✨ **Feature:** Updated model selection and validated against available models in KOALA provider (#701563f)
- ✨ **Feature:** Updated available models and removed logging functionality in Jadve provider (#be93810)
- ✨ **Feature:** Updated User-Agent to use LitAgent for dynamic generation in ChatGLM provider (#48ac416)
- 🔨 **Refactor:** Removed logging functionality from WiseCat and YEPCHAT classes (#c503120)
- 🔨 **Refactor:** Removed logging capabilities and simplified initialization in GliderAI and DeepInfra providers (#7f4b98b)
- ✨ **Feature:** Added PerplexityLabs to provider list and updated README with new model (#bf82326)
- ✨ **Feature:** Added customizable system prompt for conversation initialization in ElectronHub provider (#a1eee9e)
- ✨ **Feature:** Added ElectronHub provider supporting 371 AI models (#1a9f330)
- ✨ **Feature:** Added GitHub data extraction module with user and repository functionalities in GitAPI (#4559c60)
- ✨ **Feature:** Added AkashGPT to provider list and updated README with new model (#2d48123)
- ✨ **Feature:** Updated AVAILABLE_MODELS list by removing and adding new models in FreeAIChat provider (#aa9834b)
- ✨ **Feature:** Added Genspark providers with examples and documentation updates in AISearch (#56804de)
- ✨ **Feature:** Added voice support with logging and enhanced voice configuration in PiAI provider (#56804de)
- ✨ **Feature:** Added AVAILABLE_MODELS list and updated default model with validation in DeepInfra provider (#dc340cb)

### 2024-03-02

- 🔼 **Version:** Bumped version to 7.3 (#107a59e)
- ✨ **Feature:** Enhanced AVAILABLE_MODELS with detailed descriptions for each model in TextPollinationsAI provider (#a47ef31)
- ✨ **Feature:** Added synchronous and asynchronous methods for retrieving weather information from DuckDuckGo (#b17c429)
- ✨ **Feature:** Added suggestions method to YepSearch class for autocomplete functionality (#3b1970a)
- ✨ **Feature:** Added YepSearch class for text and image search functionality (#ab1285f)
- 🛠️ **Fix:** Added missing comma in BUILD_ARTIFACTS and updated AVAILABLE_MODELS in YEPCHAT provider (#40bd2a2)

### 2024-03-01

- ✨ **Feature:** Implemented FreeAIChat provider with multi-model support (#52dd9a2)
- ✨ **Feature:** Added FreeAIImager provider with DALL-E 3 & Flux models (#ca6a4c3)
  - Implemented new TTI provider with support for 7 premium models
  - Added both sync (FreeAIImager) and async (AsyncFreeAIImager) classes
  - Included comprehensive documentation and usage examples
  - Supported models: DALL-E 3, Flux Pro Ultra, Flux Pro, Flux Realism, etc.

## Version 7.2 (February 2024)

### 2024-02-25

- 🔄 **Merge:** Integrated latest changes from main branch (#4c820e9)
- 🛠️ **Fix:** Solved problem with pydantic import error in Bard provider and made replace_links_with_numbers function available (#b4a8868)

### 2024-02-24

- 🔄 **Merge:** Integrated latest changes from main branch (#09cb4ef)
- 🛠️ **Enhancement:** Enhanced logging system with new log levels, formats, and console handler improvements (#32fad16)

### 2024-02-23

- 🔄 **Merge:** Integrated latest changes from main branch (#8ee4372)
- 🛠️ **Fix:** Added resource cleanup method (#18b3a1a)
- 🔨 **Refactor:** Updated code (#ad7e21a)
- ✨ **Feature:** Implemented core logging functionality with handlers and utilities (#e175955)
- ✨ **Feature:** Added WiseCat provider (#ecb240d)

### 2024-02-22

- ✨ **Feature:** Enhanced GEMINI provider with model support and logging capabilities (#60a80f2)
- 🔄 **Update:** Updated Cerebras available models (#1f72427)
- 🔨 **Refactor:** Cleaned up docstrings and updated deprecated model mappings (#0034659)

### 2024-02-18

- ✨ **Feature:** Added new models to the GROQ provider (#e7e39c3)

### 2024-02-14

- 🔄 **Merge:** Integrated latest changes from main branch (#2b56a52)
- 🛠️ **Enhancement:** Enhanced code safety and fixed for_non_stream method in QwenLM provider (#bbbbbd3, #7291098)
  - Added ability to use different types of chats (t2t, search, t2i, t2v)

### 2024-02-13

- ✨ **Feature:** Added QwenLM provider to the list of available providers in the API (#cd03cdc)
- 🛠️ **Fix:** Updated deprecated model mappings for llama variants (#7a8d77e)

### 2024-02-10

- 🔄 **Merge:** Integrated latest changes from main branch (#4e8ab51, #71ec978, #55f6979)
- ✨ **Feature:** Added support for Claude variant in Free2GPT API client (#55f6979)
- ✨ **Feature:** Added ChatGPTGratis provider with logging and streaming capabilities (#a3ec214)
- 🛠️ **Fix:** Updated setup.py (#e5b5f0b, #6282524)

### 2024-02-10

- 🔨 **Refactor:** Updated README formatting, removed yaspin dependency, and bumped version to 7.1 (#5123775)
- ✨ **Feature:** Added models & logger (#63f6b0c)
- ✨ **Feature:** Added logging and litagent in deepinfra (#6458c31)
- ✨ **Feature:** Added logging capabilities to DGAFAI class (#726a49c)
- ✨ **Feature:** Added comprehensive logging to GliderAI class (#a1eda85)
- ✨ **Feature:** Added logging functionality to GaurishCerebras API client and modified response handling in chat and ask methods (#c28572b)
- ✨ **Feature:** Added logging functionality to JadveOpenAI class and improved code readability with comments and docstrings (#75d583b)
- ✨ **Feature:** Added LitLogger to LlamaTutor provider (#4699c82)
- ✨ **Feature:** Implemented logging in LLMChat (#50d8ae2)
- ✨ **Feature:** Enhanced Marcus provider monitoring with logging (#8496f3b)
- 🔨 **Refactor:** Replaced hardcoded user-agents with Lit().random() in webscout/Provider/meta.py (#2dbf2e8)
- ✨ **Feature:** Added logging capabilities to MultiChatAI class, improved code organization and readability, and added new models (#e51bad3)
- ✨ **Feature:** Updated model list and improved response handling in blackbox provider (#359384a)
- ✨ **Feature:** Enhanced Netwrck provider logging and models (#b1ee3f1)
- ✨ **Feature:** Enhanced PizzaGPT provider with web search capability and improved logging (#2aeceb9)
- 🔨 **Refactor:** Used dynamic User-Agent in TextPollinationsAI class (#83dfb85)
- ✨ **Feature:** Added logging capabilities to TextPollinationsAI class (#174ee5b)
- ✨ **Feature:** Enhanced PI provider logging and voice (#a921ddc)
- 🔄 **Update:** Updated available model in YEPCHAT provider (#9eb38f9)
- 🔄 **Update:** Updated GROQ provider models in Groq.py (#8ace3c1)

### 2024-02-09

- 🔄 **Merge:** Integrated latest changes from main branch (#9f70daf)
- ✨ **Feature:** Added new model o3-mini (#0b1fa05)

### 2024-02-08

- 🔨 **Refactor:** Removed RUBIKSAI provider and updated imports (#f57b40d)
- 🔄 **Update:** Added new models to TextPollinationsAI provider (#1dfcb89)

### 2024-02-07

- ✨ **Feature:** Added support for new models and improved error handling in TypeGPT API interactions (#3bf75f1)
- 🔨 **Refactor:** Refactored LLAMA3 class to Sambanova class with updated API interactions and streaming support (#34a4ff6)
- 🔄 **Update:** Updated LLM model in example usage to Mistral-Small-24B-Instruct-2501 (#f4b6fc4)

### 2024-02-05

- 🔄 **Update:** Updated version number in webscout/version.py from 6.9 to 7.0 (#0611fbd)
- ✨ **Feature:** Added DGAFAI provider (#be82d8d)

### 2024-02-02

- 🔄 **Update:** Added new model to LLMChat provider (#eeb2bd5)
- ✨ **Feature:** Added GliderAI provider and updated README (#2ff86ac)
- 🔄 **Update:** Updated available models and enhanced payload structure for improved API interaction in YouChat provider (#2b26df6)
- 🔄 **Merge:** Integrated latest changes from main branch (#692778a)
- ✨ **Feature:** Added TextPollinationsAI provider and enhanced get_current_app function for cross-platform support (#4c0ca77)

### 2024-02-02

- 🔄 **Merge:** Integrated latest changes from main branch (#42421b6)
- 🛠️ **Fix:** Fixed Blackbox chat endpoint (#7423f6c)

## Version 7.1 (January 2024)

### 2024-01-23

- ✨ **Feature:** Added new AI search providers DeepFind and NousHermes (#7423f6c)
  - Updated README with usage examples

### 2024-01-21

- ✨ **Feature:** Added DeepFind provider and refactored Felo to use AISearch (#b79e9e1)

### 2024-01-20

- 🔼 **Version:** Bumped version to 6.9 (#7b996fb)
- 🔨 **Refactor:** Enhanced async implementation with improved rate limiting (#545f751)

### 2024-01-13

- 🛠️ **Fix:** Fixed bug in yttoolkit (#3de3e7c)

### 2024-01-10

- 🔼 **Version:** Bumped version to 6.8 (#d7e01b9)

### 2024-01-07

- 🔄 **Merge:** Integrated latest changes from main branch (#eb91f5b)
- 🛠️ **Fix:** Fixed various issues (#3361946)

## Version 7.0 (December 2023)

### 2023-12-31

- 🛠️ **Fix:** Fixed PI AI is_conversation = False problem (#002db8d)

### 2023-12-28

- 🔼 **Version:** Bumped version to 6.7 (#e457856)

### 2023-12-25

- 🛠️ **Fix:** Fixed Python 3.7 syntax compatibility (#66d9dd9)

### 2023-12-23

- 🔄 **Merge:** Integrated latest changes from main branch (#5c2360c)
- 🛠️ **Fix:** Fixed bugs in CLI (#79f437d)
- 🛠️ **Fix:** Fixed issue with Network provider (#29e173b)

### 2023-12-22

- 🔄 **Merge:** Integrated latest changes from main branch (#029553b)
- 🛠️ **Fix:** Fixed error during creation of executable file (#7eba880)

### 2023-12-21

- 🔼 **Version:** Bumped version to 6.6 (#6e3ec97)

### 2023-12-17

- 🔄 **Merge:** Integrated latest changes from main branch (#3b749fd)
- 🛠️ **Enhancement:** Updated optimizers (#33a2b2d)
- 📝 **Documentation:** Updated README.md (#62df18f)

### 2023-12-16

- 🔄 **Update:** Moved felo to AISEARCH (#921ffac)
- ✨ **Feature:** Added JadveOpenAI provider (#f91bebc)

### 2023-12-15

- ✨ **Feature:** Added support for intro and act in TeachAnything (#ce4fd41)
- 🔨 **Refactor:** Added litagent for user agent in turboseek (#7a3ae08)
- 🛠️ **Fix:** Fixed typo (#ff3d6a8)
- 🔨 **Refactor:** Removed html_to_terminal function and its usages from tutorai.py (#32516c8)
- 🗑️ **Remove:** Deprecated AIuncensored provider (#1e4e49a)
- 🗑️ **Remove:** Deprecated upstage provider (#479266f)

### 2023-12-14

- 📝 **Documentation:** Updated x0gpt.py with lit docstrings and examples (#666a9c2)
- 📝 **Documentation:** Updated YEPCHAT docstrings with examples (#6464032)
- 🔄 **Update:** Set claude_3_5_haiku as default model in YouChat provider and adjusted personalization settings (#8c3a01e)
- 🗑️ **Remove:** Deprecated perplexity and genspark providers (#a32bd8b)
- ✨ **Feature:** Added MultiChatAI provider and fixed typo (#e93f4c3)

### 2023-12-11

- 🔄 **Merge:** Integrated latest changes from main branch (#93d14a9)
- 🛠️ **Fix:** Fixed various issues (#d62a6dd)

### 2023-12-08

- ✨ **Feature:** Added Netwrck provider (#b54bee3)

### 2023-12-07

- 🔨 **Refactor:** Simplified imports and removed zerodir dependency in AIutel.py (#64f4249)
- 🔨 **Refactor:** Converted ZeroDirs to string path for os.path.exists compatibility (#24df2d5)
- 🔨 **Refactor:** Fixed zerodir import and usage in AIutel.py (#3eced35)

### 2023-12-07

- 🔼 **Version:** Bumped version to 6.5 (#55dc08b)
- 📝 **Documentation:** Added MarkdownLite feature link to README.md (#fca6488)
- 🔨 **Refactor:** Replaced appdirs with zerodir in AIutel.py and removed appdirs from setup.py (#9a4eded)
- 🔨 **Refactor:** Replaced BeautifulSoup with Scout in meta.py, updated DWEBS.py, and other module improvements (#3a3afa1)
- 🔄 **Merge:** Resolved merge conflict in deepgram.py, keeping custom sentence splitting implementation (#7f040c7)
- 🔄 **Update:** Updated Deepgram TTS provider (#7771cb0)

### 2024-12-07

- 🔄 **Merge:** Integrated latest changes from main branch (#74acc95)
- ✨ **Feature:** Integrated Official Voices of PiAI for Enhanced Interaction (#a137e6b)
- ✨ **Feature:** Integrated MurfAITTS, GesseritTTS (#25ca929)
- 🔨 **Refactor:** Updated setup.py (#d3dbafc)
- ✨ **Feature:** Integrated Elevenlabs TTS (#5ac2c16)

### 2024-12-05

- 🔄 **Merge:** Integrated latest changes from main branch (#d55e422)
- ✨ **Feature:** Integrated Deepgram TTS (#dd7dfb0)

## Version 6.4 (November 2024)

### 2024-11-21

- 🛠️ **Fix:** Fixed various issues (#869c452)

### 2024-11-15

- 📝 **Documentation:** Created FUNDING.yml (#bf3b1fc)
- 📝 **Documentation:** Updated issue templates (#63dcba8, #5af8114)

### 2024-11-08

- 🛡️ **Security:** Added safety settings in gemini API (#b4d626d, #d8ce65d)

### 2024-11-01

- 🔼 **Version:** Bumped version to 6.2 (#7ff6ca0)

### 2024-10-27

- 🔄 **Update:** Updated cerebras.py (#84c3731)
- ✨ **Feature:** Added new providers (#a1dc109, #c67543c)

### 2024-10-16

- ✨ **Feature:** Added new project (#8b10ab9)

### 2024-10-02

- 🛠️ **Fix:** Fixed stream (#63b0508)

### 2024-09-27

- 📝 **Documentation:** Updated README.md (#b204272, #e67b51e)

### 2024-09-26

- 📝 **Documentation:** Updated README.md (#33d640d, #ff57a73, #e50244c)

### 2024-09-23

- 🔼 **Version:** Bumped version to 5.8 (#be481a3)

### 2024-09-15

- 🔼 **Version:** Bumped version to 5.7 (#f6efc42)
- 🔼 **Version:** Bumped version to 5.6 (#cd26f86)

### 2024-09-10

- 🗑️ **Remove:** Deprecated helpingai-t2 provider (#dd481f2, #c5dd704)

### 2024-09-04

- ✨ **Feature:** Added Lepton, GEMINIAPI, Cleeai, Elmo, Genspark providers (#61b1c04)

### 2024-08-30

- 🔨 **Refactor:** Removed unused imports (#146ee41)

### 2024-08-28

- 🔼 **Version:** Bumped version to 5.3 (#f04039c)
- 🛠️ **Fix:** Fixed various issues (#161481b)
- ✨ **Feature:** Added new providers (#e3e1afa)
- 🛠️ **Fix:** Fixed streaming (#187ea3f)
- 🗑️ **Remove:** Deprecated Berlin4h provider (#0f0de5e)
- 🛠️ **Fix:** Fixed HTML tags (#2d40c18)
- 🛠️ **Fix:** Fixed repetitions (#5a87832)
- 🔄 **Update:** Updated transcriber (#6e5ccec)

### 2024-08-25

- ✨ **Feature:** Added TTS, TTI providers (#923192f)

### 2024-08-24

- ✨ **Feature:** Added TTI and more (#ba12eda)

### 2024-08-21

- 🛠️ **Fix:** Fixed ollama and added support for autollama on WSL and Windows (#ccb8b18, #dfc310b)

### 2024-08-18

- 🔄 **Update:** Updated function call (#5a00d9b)

### 2024-08-15

- 🔼 **Version:** Bumped version to 4.9 (#90cac0e)

### 2024-08-14

- 🛠️ **Fix:** Fixed various issues (#8d674f2)

### 2024-08-13

- ✨ **Feature:** Added Julius provider (#bc7f588)
- ✨ **Feature:** Added xdash provider (#847071a)
- 🔄 **Merge:** Resolved merge conflict in t.py (#21db125)
- ✨ **Feature:** Added new files (#2cb07e4)

### 2024-08-12

- 📝 **Documentation:** Updated README.md (#4b6f843, #0ddc650)

### 2024-08-06

- ✨ **Feature:** Added meta AI provider (#5ce8ce4)

### 2024-08-04

- 🛠️ **Fix:** Fixed various issues and added new providers (#8db4177, #d0309fa)

### 2024-07-30

- 🔼 **Version:** Bumped version to 4.5 (#8f1fa23)
- ✨ **Feature:** Added new files (#c43f467, #569ca7e, #da2ce19, #ea8e66f, #c027dca)

### 2024-07-18

- 🛠️ **Fix:** Fixed and added ollama provider (#37a4018, #4e9878c)

### 2024-07-15

- 🔄 **Update:** Made minor changes (#d9cb348)

### 2024-07-14

- ✨ **Feature:** Updated CLI (#adefd99, #c4f5baa)

### 2024-07-13

- ✨ **Feature:** Added UI (#401ff60)
- 🔄 **Update:** Made some changes (#c20a0f9)
- 🛠️ **Fix:** Fixed small bug (#744f7ed)
- 🔄 **Update:** Made some improvements in Webscout (#1e130c9)

### 2024-07-12

- 🔄 **Update:** Made changes (#b2bb531)

### 2024-07-08

- ✨ **Feature:** Added new provider and fixed llama (#25f19d3)

### 2024-07-06

- ✨ **Feature:** Added Ollama provider (#256f484)

### 2024-07-04

- ✨ **Feature:** Added all non-api providers to AIauto (#84c6b0e, #01113c5)

### 2024-07-03

- 🔼 **Version:** Bumped version to 4.0 (#53ad7b9)

### 2024-07-02

- ✨ **Feature:** Updated CLI and added ytdownloader, weather (#fa901cf, #979671f)

### 2024-07-01

- ✨ **Feature:** Added weather fetch (#36f43a1)

### 2024-06-28

- 🛠️ **Fix:** Fixed various issues (#a253e29)
- ✨ **Feature:** Added more providers and optimized rawdog (#650626e)

### 2024-06-27

- 🔄 **Update:** Updated test.py (#dfe5a99)

### 2024-06-26

- ✨ **Feature:** Added new files (#169fd79, #6e066e3, #67924d3, #f41563e, #cd31247, #8e5fa54, #732d07a, #cb7e3cf, #b674170, #af8b162, #3cc6c49, #cc6c55e, #92449a7, #8b1f698, #837fb99)

### 2024-06-22

- 🔼 **Version:** Bumped version to 3.6 (#363d0f0)
- ✨ **Feature:** Added error fixer for internal rawdog (#fcb29c0, #38b45aa)
- ✨ **Feature:** Added phind and opengptv2 providers (#cff1c1b)

### 2024-06-16

- ✨ **Feature:** Added VLM, deepinfra, WEBSX providers and fixed DWEBS (#8a3418b, #1856287)

### 2024-06-14

- 🛠️ **Fix:** Fixed various issues (#c5fa438)

### 2024-06-06

- 🔄 **Update:** Updated history (#e3120ac)

### 2024-06-04

- ✨ **Feature:** Added new project (#06a027a)

### 2024-06-03

- ✨ **Feature:** Added rawdog to local (#c743c02)

### 2024-05-30

- 🗑️ **Remove:** Deleted build/lib directory (#0543861)
- ✨ **Feature:** Added function calling (#68ae561)

### 2024-05-26

- 🔼 **Version:** Bumped version to 2.9 (#cd78641)

### 2024-05-21

- 🛠️ **Fix:** Fixed various issues (#7b5b7e3, #26002be)

### 2024-05-19

- 🛠️ **Fix:** Solved small issues (#cf82395, #233986c)

### 2024-05-16

- 🔄 **Update:** Updated **init**.py (#112088e)

### 2024-05-15

- ✨ **Feature:** Added new project (#6e089bc)

### 2024-05-14

- 🛠️ **Fix:** Fixed various issues (#8ae0edb, #dfbd426)
- 🔼 **Version:** Bumped version to 2.4 (#416cc94)
- 🔄 **Merge:** Integrated latest changes from main branch (#6ebbaba)
- ✨ **Feature:** Added auto download to local (#066d389)

### 2024-05-13

- 🛠️ **Fix:** Solved small issues (#3be3272, #56643b1)

### 2024-05-12

- 🔄 **Merge:** Integrated latest changes from main branch (#2e93920)
- ✨ **Feature:** Added 2 new AI providers (#b776b0a)

### 2024-05-11

- 📝 **Documentation:** Created FUNDING.yml (#cfd6003)
- 📝 **Documentation:** Updated issue templates (#21491cf, #2be175b)
- 🔼 **Version:** Bumped version to 2.0 (#111059f, #4ca1d2c, #a22b477)
- ✨ **Feature:** Added auto provider (#338fce3, #fc6c6d0)

### 2024-05-10

- 🛠️ **Fix:** Fixed various issues (#6d9be23, #3d336c2, #9b1d029)
- ✨ **Feature:** Added thinkanyai provider (#a9dcf39)

### 2024-05-09

- 🛠️ **Fix:** Solved small issues (#addd1b0)

### 2024-05-08

- 📝 **Documentation:** Updated README.md (#ac350b8)
- 🔼 **Version:** Bumped version to 1.4.3 (#6986cd5)
- ✨ **Feature:** Added gpt 3.5 provider (#55ea2b3)
- 🛠️ **Fix:** Solved issue with youchat (#db4a122)

### 2024-05-06

- 🔄 **Update:** Updated setup.py (#98fcceb, #a8a4e83, #f4e34cd)

### 2024-05-04

- ✨ **Feature:** Added temp mail and number (#3d41434)
- 📝 **Documentation:** Updated README.md (#def99db)

### 2024-05-03

- 🛠️ **Fix:** Solved small issues (#2a392a4)
- 🔄 **Update:** Updated setup.py (#61fc894)
- 🔼 **Version:** Bumped version to 1.3.9 (#f0f701c)

### 2024-04-27

- 🔼 **Version:** Bumped version to 1.3.8 (#43365b6)

### 2024-04-26

- ✨ **Feature:** Added new provider (#7f04d08)
- ✨ **Feature:** Added new files (#f83bbc4, #1c85e56, #5ac8675)

### 2024-04-22

- 🗑️ **Remove:** Deleted .circleci directory (#b20e03b)
- 🔄 **Update:** Updated setup.py (#04ed965, #b71f1ab, #002e931, #16dc95f)
- 🔄 **Merge:** Integrated latest changes from main branch (#9f22f9a)
- ✨ **Feature:** Added CircleCI commit (#b53ff01)

### 2024-04-20

- 🛠️ **Fix:** Solved typing error in setup.py (#b688112)
- 🛠️ **Fix:** Solved typing error in webai (#0a9591a)
- 🔄 **Merge:** Integrated latest changes from main branch (#eec1b00)
- ✨ **Feature:** Added webai and solved some issues (#a8a3c01, #20f5c7a)

### 2024-04-19

- ✨ **Feature:** Added new files (#d37229c)
- 🛠️ **Fix:** Solved LLM issue and added v1.3.3 (#5bf2c02, #9dbd955, #953e3c6)
- 🔄 **Update:** Updated **init**.py (#27f7fb2)
- 🔄 **Update:** Updated setup.py (#186e6fe)
- ✨ **Feature:** Added sean and testing webai (#b663a4b)
- ✨ **Feature:** Added new LLM models and solved issues related to appdirs (#86bdc4b)

### 2024-04-16

- ✨ **Feature:** Added TTS in webscout (#8b481ab, #1131463)

### 2024-04-12

- 🛠️ **Fix:** Fixed small issues (#fad2ba4)

### 2024-04-11

- 🔄 **Update:** Updated **init**.py (#aeb79c2)
- 📝 **Documentation:** Updated AsyncWEBS example code (#cfb4b96)

### 2024-04-09

- 🔼 **Version:** Bumped version to 1.2.8 (#0ce7881)

### 2024-04-07

- ✨ **Feature:** Added transcriber (#59f0b2f)

### 2024-04-03

- 🗑️ **Remove:** Deprecated offline AI and added KOBOLDAI (#83de7b9)

### 2024-04-02

- ✨ **Feature:** Added offline AI via gpt4all (#769bc88)

### 2024-03-31

- 📝 **Documentation:** Renamed CONTRIBUTING.md to CONTRIBUTE.md (#7c52f6b)
- 📝 **Documentation:** Created CONTRIBUTING.md (#0b0e59a)
- 🗑️ **Remove:** Deleted **pycache** directory (#d7c1eff)
- 🛠️ **Fix:** Added error handling in deepwebs and solved some issues (#61c6f73)
- 🗑️ **Remove:** Deleted DeepWEBS/files directory (#aa15feb)

### 2024-03-30

- ✨ **Feature:** Added DeepWEBS (#2e9c94a)
- 🔼 **Version:** Bumped version to 1.2.1 (#fd0a6c3)
- 🔼 **Version:** Bumped version to 1.2.0 (#1f8f4d9)
- 🔼 **Version:** Bumped version to 1.1.9 (#cb71ad4)

### 2024-03-29

- 🗑️ **Remove:** Deleted webscout-api/README.md (#bdb0da5)
- 🔄 **Update:** Updated flasksapi.py (#8c01ec5)
- 🗑️ **Remove:** Deleted webscout-api/API.py (#36b083d)

### 2024-03-24

- 🛠️ **Fix:** Solved issue (#ff58f52)
- 🛠️ **Fix:** Solved issue with CLI and added some cool things (#686cd0e, #14f7ca9)
- ✨ **Feature:** Added webscout new version (#cf400cf)
- ✨ **Feature:** Added openGPT (#79ba15e)
- ✨ **Feature:** Added perplixity (#56c929f)
- ✨ **Feature:** Added BlackBox and solved issue with phind (#1fbfbae)

### 2024-03-15

- ✨ **Feature:** Added new files (#a699f61)

### 2024-03-10

- 🛠️ **Fix:** Solved issue (#885b5fa)

### 2024-03-06

- 📝 **Documentation:** Updated README.md (#cdaf96d, #7d5b05c, #f71ef0d)
- 🗑️ **Remove:** Deleted API.md (#9f5d2ba)
- 📝 **Documentation:** Created API.md (#b5e2f7b, #b638fbe)
- ✨ **Feature:** Added webscout API (#65a56c4)
- 🔄 **Update:** Updated setup.py (#944c77d)
- 🗑️ **Remove:** Deleted HelpingAI.py (#bdd185e)
- ✨ **Feature:** Added new files (#046a45a, #53699a9)
- 🔼 **Version:** Bumped version to 1.0.4 (#a3664e5)
- 🛠️ **Fix:** Solved gemmni and added new features (#a49d072)
- ✨ **Feature:** Added HelpingAI and solved some issues (#b85c733)

### 2024-02-28

- 🗑️ **Remove:** Deleted test.py (#6d6af38)
- 🛠️ **Fix:** Solved gemmni (#7d386b5)
- ✨ **Feature:** Added LLM (#920c488)
- ✨ **Feature:** Added Prodia as image generator in webscout.AI (#22cafc7)
- 🔄 **Update:** Updated setup.py (#46f0f3a)

### 2024-02-27

- 📝 **Documentation:** Updated README.md (#c12f1f0, #1385a40, #ecac419, #e0ad836, #50acc32, #f122fdd)
- 🔄 **Update:** Updated setup.py (#c394c45, #b959c6a, #f2204bd, #2879782)

## Version 6.0 (January 2024)

### 2024-01-31

- ✨ **Feature:** Added new features and improvements (#4a80cce)