# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.23.0 from ../specs/llm-prompt.spec.md
# (spec:b0bb74ef) (code:90c30f44)

import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import llm_prompt

def test_main_success(monkeypatch, capsys):
    test_prompt = "Hello world"
    monkeypatch.setattr(llm_prompt, "load_api_key", lambda: "fake-api-key")
    monkeypatch.setattr(llm_prompt, "load_model", lambda: "gemini-1.5-pro")
    monkeypatch.setattr(llm_prompt, "send_prompt_to_gemini", lambda prompt, api_key, model: "mocked response")
    monkeypatch.setattr(sys, "argv", ["llm-prompt", test_prompt])

    # Should complete normally without raising SystemExit
    llm_prompt.main()

    captured = capsys.readouterr()
    assert captured.out.strip() == "mocked response"
