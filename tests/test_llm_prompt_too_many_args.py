# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.23.0 from ../specs/llm-prompt.spec.md
# (spec:b0bb74ef) (code:b1d02dff)

import pytest
import sys
from unittest.mock import patch, MagicMock
from src.llm_prompt import main

def test_too_many_args():
    """Test that providing more than one argument prints usage error and exits with non-zero code."""
    test_args = ['llm-prompt', 'arg1', 'arg2']
    
    with patch.object(sys, 'argv', test_args):
        with pytest.raises(SystemExit) as exc_info:
            with patch('builtins.print') as mock_print:
                main()
        
        # Verify non-zero exit code
        assert exc_info.value.code != 0
        
        # Verify usage error message was printed
        mock_print.assert_called()
        printed_message = str(mock_print.call_args[0][0]).lower()
        assert 'usage' in printed_message or 'error' in printed_message
