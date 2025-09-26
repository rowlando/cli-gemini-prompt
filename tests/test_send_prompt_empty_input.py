# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.23.0 from ../specs/llm-prompt.spec.md
# (spec:06252042) (code:665eee41)

import os
import sys
import pytest
from unittest.mock import Mock, patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import llm_prompt

def test_send_prompt_empty_input():
    """Test that send_prompt_to_gemini processes empty prompt through LangChain correctly."""
    
    # Mock the ChatGoogleGenerativeAI and its invoke method
    mock_chat_instance = Mock()
    mock_response = Mock()
    mock_response.content = "Empty prompt response"
    mock_chat_instance.invoke.return_value = mock_response
    
    with patch('llm_prompt.ChatGoogleGenerativeAI', return_value=mock_chat_instance):
        result = llm_prompt.send_prompt_to_gemini("", "fake-api-key", "gemini-1.5-pro")
        
        # Verify the response is returned correctly
        assert result == "Empty prompt response"
        
        # Verify ChatGoogleGenerativeAI was created with correct parameters
        llm_prompt.ChatGoogleGenerativeAI.assert_called_once_with(
            model="gemini-1.5-pro",
            google_api_key="fake-api-key"
        )
        
        # Verify invoke was called with empty string
        mock_chat_instance.invoke.assert_called_once_with("")
