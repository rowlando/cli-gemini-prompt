# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.23.0 from ../specs/llm-prompt.spec.md
# (spec:06252042) (code:2d21f1fc)

import os
import sys
import pytest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import llm_prompt

def test_llm_prompt_missing_api_key(capsys):
    test_args = ['llm-prompt', 'test prompt']
    with patch('sys.argv', test_args), \
         patch('llm_prompt.load_dotenv'), \
         patch.dict(os.environ, {}, clear=True):
        with pytest.raises(SystemExit) as exc_info:
            llm_prompt.main()
    assert exc_info.value.code != 0
    captured = capsys.readouterr()
    assert "API key" in captured.err
