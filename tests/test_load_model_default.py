# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.23.0 from ../specs/llm-prompt.spec.md
# (spec:06252042) (code:2c7139c7)

import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import llm_prompt

def test_load_model_default(monkeypatch):
    # Mock load_dotenv to prevent loading from .env file
    monkeypatch.setattr(llm_prompt, 'load_dotenv', lambda: None)
    # Clear the environment variable
    monkeypatch.delenv('DEFAULT_MODEL', raising=False)
    result = llm_prompt.load_model()
    assert result == "gemini-1.5-pro"
