# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.23.0 from ../specs/llm-prompt.spec.md
# (spec:06252042) (code:f66aa118)

import os
import sys
import pytest
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import llm_prompt

def test_send_prompt_langchain_error():
    """Test that LangChain API exceptions are re-raised by send_prompt_to_gemini."""
    
    # Create a mock exception that would come from LangChain
    mock_exception = Exception("LangChain API error")
    
    # Mock the ChatGoogleGenerativeAI to raise an exception when invoke is called
    with patch('llm_prompt.ChatGoogleGenerativeAI') as mock_chat_class:
        mock_chat_instance = MagicMock()
        mock_chat_instance.invoke.side_effect = mock_exception
        mock_chat_class.return_value = mock_chat_instance
        
        # Test that the exception is re-raised
        with pytest.raises(Exception) as exc_info:
            llm_prompt.send_prompt_to_gemini("test prompt", "fake-api-key", "gemini-1.5-pro")
        
        # Verify the exception message includes the wrapped error
        assert str(exc_info.value) == "Failed to get response from Gemini: LangChain API error"
        
        # Verify the ChatGoogleGenerativeAI was initialized with correct parameters
        mock_chat_class.assert_called_once_with(
            model="gemini-1.5-pro",
            google_api_key="fake-api-key"
        )
        
        # Verify invoke was called with the prompt
        mock_chat_instance.invoke.assert_called_once_with("test prompt")
