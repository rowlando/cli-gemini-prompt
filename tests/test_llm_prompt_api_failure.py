# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.23.0 from ../specs/llm-prompt.spec.md
# (spec:06252042) (code:606c108d)

import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "src")))
import llm_prompt

def test_llm_prompt_api_failure(monkeypatch, capsys):
    # simulate command-line arguments
    monkeypatch.setattr(sys, "argv", ["llm-prompt", "Hello world"])
    # patch load_api_key to return a dummy key
    monkeypatch.setattr(llm_prompt, "load_api_key", lambda: "dummy_key")
    # patch load_model to return a dummy model
    monkeypatch.setattr(llm_prompt, "load_model", lambda: "gemini-1.5-pro")
    # patch send_prompt_to_gemini to raise an exception
    def fake_send(prompt, api_key, model):
        raise Exception("Gemini API error")
    monkeypatch.setattr(llm_prompt, "send_prompt_to_gemini", fake_send)
    
    with pytest.raises(SystemExit) as excinfo:
        llm_prompt.main()
    
    assert excinfo.value.code != 0
    captured = capsys.readouterr()
    output = captured.out + captured.err
    assert "Gemini API error" in output
