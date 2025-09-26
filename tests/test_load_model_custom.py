# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.23.0 from ../specs/llm-prompt.spec.md
# (spec:06252042) (code:873ab043)

import os
import sys
import pytest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import llm_prompt

def test_load_model_custom(monkeypatch):
    """Test that load_model returns custom model when DEFAULT_MODEL is set in environment."""
    monkeypatch.setenv("DEFAULT_MODEL", "gemini-1.5-flash")
    
    result = llm_prompt.load_model()
    
    assert result == "gemini-1.5-flash"
