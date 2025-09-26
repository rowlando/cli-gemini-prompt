# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.23.0 from ../specs/llm-prompt.spec.md
# (spec:06252042) (code:3e8aedd0)

import os
import sys
import pytest
from unittest.mock import patch, Mock
from requests.exceptions import ConnectionError, Timeout

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import llm_prompt

def test_network_failure_handling(monkeypatch, capsys):
    """Test that network failures are handled appropriately and exit with non-zero code"""
    # Mock the dependencies to get to the network failure point
    monkeypatch.setattr(llm_prompt, "load_api_key", lambda: "fake-api-key")
    monkeypatch.setattr(llm_prompt, "load_model", lambda: "gemini-1.5-pro")
    
    # Mock send_prompt_to_gemini to raise a ConnectionError (network failure)
    def mock_send_prompt(*args, **kwargs):
        raise ConnectionError("Network connection failed")
    
    monkeypatch.setattr(llm_prompt, "send_prompt_to_gemini", mock_send_prompt)
    monkeypatch.setattr(sys, "argv", ["llm-prompt", "test prompt"])
    
    # Should exit with non-zero code
    with pytest.raises(SystemExit) as exc_info:
        llm_prompt.main()
    
    assert exc_info.value.code != 0
    
    # Check that appropriate error message was printed
    captured = capsys.readouterr()
    assert "Network connection failed" in captured.err or "Network connection failed" in captured.out

def test_timeout_failure_handling(monkeypatch, capsys):
    """Test that timeout errors are handled appropriately and exit with non-zero code"""
    # Mock the dependencies to get to the timeout failure point
    monkeypatch.setattr(llm_prompt, "load_api_key", lambda: "fake-api-key")
    monkeypatch.setattr(llm_prompt, "load_model", lambda: "gemini-1.5-pro")
    
    # Mock send_prompt_to_gemini to raise a Timeout error
    def mock_send_prompt(*args, **kwargs):
        raise Timeout("Request timed out")
    
    monkeypatch.setattr(llm_prompt, "send_prompt_to_gemini", mock_send_prompt)
    monkeypatch.setattr(sys, "argv", ["llm-prompt", "test prompt"])
    
    # Should exit with non-zero code
    with pytest.raises(SystemExit) as exc_info:
        llm_prompt.main()
    
    assert exc_info.value.code != 0
    
    # Check that appropriate error message was printed
    captured = capsys.readouterr()
    assert "Request timed out" in captured.err or "Request timed out" in captured.out
