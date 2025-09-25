# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.23.0 from ../specs/llm-prompt.spec.md
# (spec:b0bb74ef) (code:17a3085f)

import sys
import pytest
from unittest.mock import patch
import llm_prompt

def test_send_prompt_success():
    # Mock send_prompt_to_gemini to return the expected response
    with patch.object(llm_prompt, 'send_prompt_to_gemini', return_value="mocked response") as mock_send:
        result = llm_prompt.send_prompt_to_gemini("Hello world", "fake_key", "gemini-1.5-pro")
        assert result == "mocked response"
        mock_send.assert_called_once_with("Hello world", "fake_key", "gemini-1.5-pro")
