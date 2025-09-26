# Knowledge Index

## Testing Best Practices

### Test Design Principles

**Avoid Circular Mock Tests**
- Don't mock the exact function you're testing - this only proves the mock works
- Example of poor test: `mock_function.return_value = "expected"` then `assert function() == "expected"`
- Instead: Mock dependencies and external services, test the actual function logic

**Test Real Functionality**
- Unit tests should test actual business logic, not just mock interactions
- Integration tests should use real instances of classes/services when possible
- Mock external dependencies (APIs, databases) but test your own code paths

**Prioritize Test Types**
1. **Unit Tests**: Test individual functions with mocked dependencies
2. **Integration Tests**: Test component interactions with real objects
3. **End-to-End Tests**: Test complete workflows from CLI to output

### Common Anti-Patterns to Avoid

**Over-Mocking**
- Mocking everything makes tests brittle and meaningless
- Only mock external dependencies, not your own functions under test

**Insufficient Edge Case Coverage**
- Test empty inputs, malformed data, network failures
- Test error conditions and boundary conditions
- Don't just test the happy path

**Missing Integration Coverage**
- Ensure external library integrations are tested
- Verify configuration and initialization logic
- Test actual API calls in controlled environments

### Recommended Test Structure

**For CLI Tools:**
- Test argument parsing and validation
- Test configuration loading (environment variables, files)
- Test core business logic separately from CLI interface
- Test error handling and exit codes
- Use subprocess tests for full CLI execution

**For API Integration:**
- Test with real API client instances (mocked at HTTP level)
- Verify request construction and response parsing
- Test authentication and error handling
- Include timeout and network failure scenarios

