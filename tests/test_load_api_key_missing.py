# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.23.0 from ../specs/llm-prompt.spec.md
# (spec:b0bb74ef) (code:e68f96f4)

import pytest
import os
from unittest.mock import patch, mock_open
import sys
sys.path.append('../src')
from llm_prompt import load_api_key


def test_load_api_key_missing(capsys):
    """Test that load_api_key raises SystemExit when GOOGLE_API_KEY is missing from .env"""
    # Mock the .env file without GOOGLE_API_KEY
    mock_env_content = "OTHER_KEY=other_value\n"

    with patch("builtins.open", mock_open(read_data=mock_env_content)):
        with patch("os.path.exists", return_value=True):
            with patch.dict(os.environ, {}, clear=True):
                with pytest.raises(SystemExit) as exc_info:
                    load_api_key()

                # Verify it exits with non-zero code
                assert exc_info.value.code != 0

                # Check that error message was printed to stderr
                captured = capsys.readouterr()
                assert "API key" in captured.err or "GOOGLE_API_KEY" in captured.err
