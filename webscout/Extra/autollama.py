import subprocess
import argparse

def autollama(model_path, gguf_file):
    # Initialize command list
    command = [
        "bash", "-c",
        f'''
        #!/bin/bash

        function show_art() {{
            cat << "EOF"
            Made with love in India
            EOF
        }}

        show_art

        # Initialize default values
        MODEL_PATH="{model_path}"
        GGUF_FILE="{gguf_file}"

        # Display help/usage information
        usage() {{
          echo "Usage: $0 -m <model_path> -g <gguf_file>"
          echo
          echo "Options:"
          echo "  -m <model_path>    Set the path to the model"
          echo "  -g <gguf_file>     Set the GGUF file name"
          echo "  -h                 Display this help and exit"
          echo
        }}

        # Parse command-line options
        while getopts ":m:g:h" opt; do
          case ${{opt}} in
            m )
              MODEL_PATH=$OPTARG
              ;;
            g )
              GGUF_FILE=$OPTARG
              ;;
            h )
              usage
              exit 0
              ;;
            \? )
              echo "Invalid Option: -$OPTARG" 1>&2
              usage
              exit 1
              ;;
            : )
              echo "Invalid Option: -$OPTARG requires an argument" 1>&2
              usage
              exit 1
              ;;
          esac
        done

        # Check required parameters
        if [ -z "$MODEL_PATH" ] || [ -z "$GGUF_FILE" ]; then
            echo "Error: -m (model_path) and -g (gguf_file) are required."
            usage
            exit 1
        fi

        # Derive MODEL_NAME
        MODEL_NAME=$(echo $GGUF_FILE | sed 's/\(.*\)\.Q4.*/\1/')

        # Log file where downloaded models are recorded
        DOWNLOAD_LOG="downloaded_models.log"

        # Composite logging name
        LOGGING_NAME="${{MODEL_PATH}}_${{MODEL_NAME}}"

        # Check if the model has been downloaded
        function is_model_downloaded {{
            grep -qxF "$LOGGING_NAME" "$DOWNLOAD_LOG" && return 0 || return 1
        }}

        # Log the downloaded model
        function log_downloaded_model {{
            echo "$LOGGING_NAME" >> "$DOWNLOAD_LOG"
        }}

        # Function to check if the model has already been created
        function is_model_created {{
            # 'ollama list' lists all models
            ollama list | grep -q "$MODEL_NAME" && return 0 || return 1
        }}

        # Check if huggingface-hub is installed, and install it if not
        if ! pip show huggingface-hub > /dev/null; then
          echo "Installing huggingface-hub..."
          pip install -U "huggingface_hub[cli]"
        else
          echo "huggingface-hub is already installed."
        fi

        # Check if the model has already been downloaded
        if is_model_downloaded; then
            echo "Model $LOGGING_NAME has already been downloaded. Skipping download."
        else
            echo "Downloading model $LOGGING_NAME..."
            # Download the model
            huggingface-cli download $MODEL_PATH $GGUF_FILE --local-dir downloads --local-dir-use-symlinks False
            
            # Log the downloaded model
            log_downloaded_model
            echo "Model $LOGGING_NAME downloaded and logged."
        fi


        # Check if Ollama is installed, and install it if not
        if ! command -v ollama &> /dev/null; then
          echo "Installing Ollama..."
          curl -fsSL https://ollama.com/install.sh | sh
        else
          echo "Ollama is already installed."
        fi

        # Check if Ollama is already running
        if pgrep -f 'ollama serve' > /dev/null; then
            echo "Ollama is already running. Skipping the start."
        else
            echo "Starting Ollama..."
            # Start Ollama in the background
            ollama serve &

            # Wait for Ollama to start
            while true; do
                if pgrep -f 'ollama serve' > /dev/null; then
                    echo "Ollama has started."
                    sleep 60
                    break
                else
                    echo "Waiting for Ollama to start..."
                    sleep 1 # Wait for 1 second before checking again
                fi
            done
        fi


        # Check if the model has already been created
        if is_model_created; then
            echo "Model $MODEL_NAME is already created. Skipping creation."
        else
            echo "Creating model $MODEL_NAME..."
            # Create the model in Ollama
            # Prepare Modelfile with the downloaded path
            echo "FROM ./downloads/$GGUF_FILE" > Modelfile
            ollama create $MODEL_NAME -f Modelfile
            echo "Model $MODEL_NAME created."
        fi

        echo "model name is > $MODEL_NAME"
        echo "Use Ollama run $MODEL_NAME"
        '''
    ]

    # Execute the command
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    # Print the output and error in real-time
    for stdout_line in iter(process.stdout.readline, ""):
        print(stdout_line, end='')
    for stderr_line in iter(process.stderr.readline, ""):
        print(stderr_line, end='')

    # Wait for the process to complete
    process.stdout.close()
    process.stderr.close()
    return_code = process.wait()

    if return_code != 0:
        raise subprocess.CalledProcessError(return_code, command)

def main():
    parser = argparse.ArgumentParser(description='Run autollama script to manage models with Ollama and Hugging Face')
    parser.add_argument('-m', '--model_path', required=True, help='Set the path to the model')
    parser.add_argument('-g', '--gguf_file', required=True, help='Set the GGUF file name')
    args = parser.parse_args()

    try:
        autollama(args.model_path, args.gguf_file)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
