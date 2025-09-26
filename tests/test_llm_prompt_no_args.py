# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.23.0 from ../specs/llm-prompt.spec.md
# (spec:06252042) (code:d0d56d13)

import os
import sys
import pytest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import llm_prompt

def test_no_arguments_provided():
    """Test that no arguments provided prints usage error message and exits with non-zero code."""
    with patch.object(sys, 'argv', ['llm-prompt']):
        with pytest.raises(SystemExit) as exc_info:
            with patch('builtins.print') as mock_print:
                llm_prompt.main()
        
        assert exc_info.value.code != 0
        mock_print.assert_called()
        # Verify that some kind of usage/error message was printed
        printed_args = [call.args for call in mock_print.call_args_list]
        printed_text = ' '.join([str(arg) for args in printed_args for arg in args]).lower()
        assert any(word in printed_text for word in ['usage', 'error', 'argument', 'required'])
