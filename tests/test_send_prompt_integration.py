# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.23.0 from ../specs/llm-prompt.spec.md
# (spec:06252042) (code:57069258)

import os
import sys
import pytest
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import llm_prompt

def test_send_prompt_integration():
    """Test that send_prompt_to_gemini creates ChatGoogleGenerativeAI instance with correct parameters and returns response content."""
    
    # Mock the ChatGoogleGenerativeAI class and its invoke method
    mock_response = MagicMock()
    mock_response.content = "Test response from Gemini"
    
    mock_chat_instance = MagicMock()
    mock_chat_instance.invoke.return_value = mock_response
    
    with patch('llm_prompt.ChatGoogleGenerativeAI') as mock_chat_class:
        mock_chat_class.return_value = mock_chat_instance
        
        result = llm_prompt.send_prompt_to_gemini("Hello world", "test-api-key", "gemini-1.5-pro")
        
        # Verify ChatGoogleGenerativeAI was created with correct parameters
        mock_chat_class.assert_called_once_with(
            model="gemini-1.5-pro",
            google_api_key="test-api-key"
        )
        
        # Verify invoke was called with the prompt
        mock_chat_instance.invoke.assert_called_once_with("Hello world")
        
        # Verify the response content is returned
        assert result == "Test response from Gemini"
