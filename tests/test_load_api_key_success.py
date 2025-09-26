# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.23.0 from ../specs/llm-prompt.spec.md
# (spec:06252042) (code:e0269c75)

import os
import sys
import pytest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import llm_prompt

def test_load_api_key_success():
    with patch.object(llm_prompt, 'load_dotenv'):
        with patch.dict(os.environ, {'GOOGLE_API_KEY': 'test_api_key_123'}):
            result = llm_prompt.load_api_key()
            assert result == 'test_api_key_123'
