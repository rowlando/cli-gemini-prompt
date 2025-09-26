# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.23.0 from ../specs/llm-prompt.spec.md
# (spec:06252042) (code:1977556d)

import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import llm_prompt

def test_empty_prompt_handles_normally(monkeypatch, capsys):
    empty_prompt = ""
    monkeypatch.setattr(llm_prompt, "load_api_key", lambda: "fake-api-key")
    monkeypatch.setattr(llm_prompt, "load_model", lambda: "gemini-1.5-pro")
    monkeypatch.setattr(llm_prompt, "send_prompt_to_gemini", lambda prompt, api_key, model: "response to empty prompt")
    monkeypatch.setattr(sys, "argv", ["llm-prompt", empty_prompt])

    # Should complete normally without raising SystemExit
    llm_prompt.main()

    captured = capsys.readouterr()
    assert captured.out.strip() == "response to empty prompt"
