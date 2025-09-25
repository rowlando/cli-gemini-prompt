# LLM Prompt Tool

Command-line tool that accepts a text prompt and sends it to Google's Gemini LLM using LangChain, outputting the response to stdout.

## Target

[@generate](../src/llm_prompt.py)

## Capabilities

### Accept command-line prompt

Tool accepts a single text prompt as a command-line argument and processes it.

- Valid usage: `llm-prompt "Hello world"` prints the LLM response and completes normally [@test](../tests/test_llm_prompt_main_success.py)
- No arguments provided: prints usage error message and exits with non-zero code [@test](../tests/test_llm_prompt_no_args.py)
- More than one argument provided: prints usage error message and exits with non-zero code [@test](../tests/test_llm_prompt_too_many_args.py)

### Load configuration

Loads the Google API key and model configuration from the `.env` file.

- Returns the API key string when `GOOGLE_API_KEY` is mocked in environment [@test](../tests/test_load_api_key_success.py)
- Missing `GOOGLE_API_KEY` in `.env`: raises `SystemExit` with error message containing "API key" [@test](../tests/test_load_api_key_missing.py)

### Load model configuration

Loads the model name from environment variables with fallback to default.

- Returns "gemini-1.5-pro" when `DEFAULT_MODEL` is not set in environment [@test](../tests/test_load_model_default.py)
- Returns custom model when `DEFAULT_MODEL` is set in environment [@test](../tests/test_load_model_custom.py)

### Send prompt to Gemini LLM

Sends the provided prompt to the specified Gemini model using LangChain and returns the response.

- Mocked Gemini returns `"mocked response"`: prints `"mocked response"` and completes normally [@test](../tests/test_send_prompt_success.py)

### Error handling

Provides basic error handling for common failure cases.

- Missing API key at runtime: prints error message containing "API key" and exits with non-zero code [@test](../tests/test_llm_prompt_missing_api_key.py)
- Gemini API call raises an exception: prints the exception message and exits with non-zero code [@test](../tests/test_llm_prompt_api_failure.py)

## API

```python { .api }
def main() -> None:
    """Main entry point for the llm-prompt command-line tool."""
    pass

def load_api_key() -> str:
    """Load the Google API key from .env file.
    
    Returns:
        str: The API key
        
    Raises:
        SystemExit: If API key is not found
    """
    pass

def load_model() -> str:
    """Load the model name from .env file with fallback to default.
    
    Returns:
        str: The model name (defaults to "gemini-1.5-pro" if DEFAULT_MODEL not set)
    """
    pass

def send_prompt_to_gemini(prompt: str, api_key: str, model: str) -> str:
    """Send prompt to Gemini LLM and return response.
    
    Args:
        prompt: The text prompt to send
        api_key: Google API key
        model: The Gemini model name to use
        
    Returns:
        str: The LLM response
        
    Raises:
        Exception: If API call fails
    """
    pass
```

## Dependencies

### Environment variable loading

For loading the Google API key and model configuration from .env file.
[@use](python-dotenv)

### LangChain Google Gemini integration

For interfacing with Google's Gemini LLM.
[@use](langchain-google-genai)

### Command-line argument parsing

Built-in Python module for parsing command-line arguments.
[@use](sys)