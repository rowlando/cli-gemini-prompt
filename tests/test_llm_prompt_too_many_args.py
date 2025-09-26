# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.23.0 from ../specs/llm-prompt.spec.md
# (spec:06252042) (code:dc7484a0)

import os
import pytest
import sys
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import llm_prompt

def test_too_many_args():
    """Test that providing more than one argument prints usage error and exits with non-zero code."""
    test_args = ['llm-prompt', 'arg1', 'arg2']
    
    with patch.object(sys, 'argv', test_args):
        with pytest.raises(SystemExit) as exc_info:
            with patch('builtins.print') as mock_print:
                llm_prompt.main()
        
        # Verify non-zero exit code
        assert exc_info.value.code != 0
        
        # Verify usage error message was printed
        mock_print.assert_called()
        printed_args = [str(call[0][0]) for call in mock_print.call_args_list]
        printed_message = ' '.join(printed_args).lower()
        assert 'usage' in printed_message or 'error' in printed_message
