# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.23.0 from ../specs/llm-prompt.spec.md
# (spec:b0bb74ef) (code:8af31a2e)

import sys
import pytest
from unittest.mock import patch
from src.llm_prompt import main

def test_llm_prompt_missing_api_key():
    """Test that missing API key at runtime prints error and exits with non-zero code."""
    # Mock sys.argv to provide a prompt argument
    test_args = ['llm-prompt', 'test prompt']

    # Mock load_api_key to raise SystemExit as if API key is missing
    with patch('sys.argv', test_args), \
         patch('src.llm_prompt.load_api_key', side_effect=SystemExit(1)):

        # Should raise SystemExit due to missing API key
        with pytest.raises(SystemExit) as exc_info:
            main()

        # Verify non-zero exit code
        assert exc_info.value.code != 0
