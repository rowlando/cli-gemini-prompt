# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.23.0 from ../specs/llm-prompt.spec.md
# (spec:06252042) (code:fc5aee23)

import os
import sys
import pytest
from unittest.mock import patch, mock_open

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from llm_prompt import load_api_key

def test_load_api_key_missing(capsys):
    """Test that load_api_key raises SystemExit when GOOGLE_API_KEY is missing from .env"""
    mock_env_content = "OTHER_KEY=other_value\n"

    with patch("builtins.open", mock_open(read_data=mock_env_content)):
        with patch("os.path.exists", return_value=True):
            with patch.dict(os.environ, {}, clear=True):
                with pytest.raises(SystemExit) as exc_info:
                    load_api_key()

                assert exc_info.value.code != 0
                captured = capsys.readouterr()
                assert "API key" in captured.err or "GOOGLE_API_KEY" in captured.err
