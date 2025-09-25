# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.23.0 from ../specs/llm-prompt.spec.md
# (spec:1dd67722) (code:099b0afd)

#!/usr/bin/env python3
"""
LLM Prompt Tool

Command-line tool that accepts a text prompt and sends it to Google's Gemini LLM using LangChain.
"""

import sys
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


def main() -> None:
    """Main entry point for the llm-prompt command-line tool."""
    # Check if prompt was provided
    if len(sys.argv) != 2:
        print("Usage: llm-prompt \"Your prompt text here\"", file=sys.stderr)
        sys.exit(1)
    
    prompt = sys.argv[1]
    
    try:
        # Load API key
        api_key = load_api_key()
        
        # Load model
        model = load_model()
        
        # Send prompt to Gemini and get response
        response = send_prompt_to_gemini(prompt, api_key, model)
        
        # Output the response
        print(response)
        
    except SystemExit:
        # Re-raise SystemExit to preserve exit codes
        raise
    except Exception as e:
        print(f"{e}", file=sys.stderr)
        sys.exit(1)


def load_api_key() -> str:
    """Load the Google API key from .env file.
    
    Returns:
        str: The API key
        
    Raises:
        SystemExit: If API key is not found
    """
    # Load environment variables from .env file
    load_dotenv()
    
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: API key not found in .env file", file=sys.stderr)
        sys.exit(1)
    
    return api_key


def load_model() -> str:
    """Load the model name from .env file with fallback to default.
    
    Returns:
        str: The model name (defaults to "gemini-1.5-pro" if DEFAULT_MODEL not set)
    """
    # Load environment variables from .env file
    load_dotenv()
    
    model = os.getenv("DEFAULT_MODEL")
    if not model:
        return "gemini-1.5-pro"
    
    return model


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
    try:
        # Initialize the Gemini model
        llm = ChatGoogleGenerativeAI(
            model=model,
            google_api_key=api_key
        )
        
        # Send the prompt and get response
        response = llm.invoke(prompt)
        
        # Return the content of the response
        return response.content
        
    except Exception as e:
        raise Exception(f"Failed to get response from Gemini: {e}")


if __name__ == "__main__":
    main()
