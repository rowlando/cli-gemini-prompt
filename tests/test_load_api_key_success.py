# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.23.0 from ../specs/llm-prompt.spec.md
# (spec:b0bb74ef) (code:0821d3ee)

import os
import tempfile
import pytest
from unittest.mock import patch
from src.llm_prompt import load_api_key


def test_load_api_key_success():
    """Test that load_api_key returns the API key when GOOGLE_API_KEY is set in .env"""
    # Mock os.getenv to return the test API key
    with patch.dict(os.environ, {'GOOGLE_API_KEY': 'test_api_key_123'}):
        with patch('src.llm_prompt.load_dotenv'):
            result = load_api_key()
            assert result == 'test_api_key_123'
