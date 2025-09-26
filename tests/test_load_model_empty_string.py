# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.23.0 from ../specs/llm-prompt.spec.md
# (spec:06252042) (code:cee45738)

import os
import sys
import pytest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import llm_prompt

def test_load_model_empty_string():
    """Test that load_model handles empty string in DEFAULT_MODEL by falling back to default"""
    with patch.dict(os.environ, {'DEFAULT_MODEL': ''}):
        result = llm_prompt.load_model()
        assert result == "gemini-1.5-pro"
