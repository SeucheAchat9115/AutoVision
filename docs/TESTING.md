# Testing Guide

AutoVision uses pytest for comprehensive testing with different test categories and execution environments.

## Test Structure

### Test Categories

Tests are organized using pytest markers:

- `@pytest.mark.unit` - Fast unit tests (< 1s each)
- `@pytest.mark.integration` - Integration tests (< 30s each)
- `@pytest.mark.slow` - Slow tests (> 30s)
- `@pytest.mark.gpu` - Tests requiring GPU
- `@pytest.mark.youtube` - Tests requiring YouTube access
- `@pytest.mark.model` - Tests requiring ML models

### Test Files

- `tests/test_core.py` - Core functionality tests
- `tests/test_cli.py` - CLI interface tests
- `tests/test_config.py` - Configuration system tests
- `tests/conftest.py` - Shared test fixtures

## Running Tests

### Quick Start

```bash
# Install dependencies
make install

# Run all unit tests
make test-unit

# Run all tests with coverage
make test
```

### Test Execution Options

```bash
# Unit tests only (fast)
pytest tests/ -m "unit"

# Integration tests
pytest tests/ -m "integration"

# All tests except slow ones
pytest tests/ -m "not slow"

# Specific test file
pytest tests/test_core.py

# Specific test function
pytest tests/test_core.py::test_autovision_init

# Run with coverage
pytest tests/ --cov=autovision --cov-report=html

# Parallel execution
pytest tests/ -n auto
```

### Test Environment

Use `tox` for testing across multiple Python versions:

```bash
# Install tox
pip install tox

# Run tests on all supported Python versions
tox

# Run specific test environment
tox -e py311-test
tox -e py311-lint
tox -e py311-type
```

## Development Testing

### Watch Mode

For continuous testing during development:

```bash
# Install pytest-watch
uv add pytest-watch --dev

# Run tests in watch mode
make test-watch
```

### Pre-commit Testing

Tests run automatically before commits via pre-commit hooks:

```bash
# Install pre-commit hooks
make install-pre-commit

# Run pre-commit manually
pre-commit run --all-files
```

## CI/CD Testing

### GitHub Actions

- **CI Pipeline** (`.github/workflows/ci.yml`):
  - Runs on every push and PR
  - Includes linting, type checking, and unit tests
  - Supports multiple Python versions

- **PR Testing** (`.github/workflows/test-pr.yml`):
  - Quick tests for PR validation
  - Full test suite on labeled PRs

- **Nightly Tests** (`.github/workflows/nightly.yml`):
  - Comprehensive testing across OS/Python combinations
  - Performance benchmarks and security audits

### Test Coverage

Coverage reports are generated and uploaded to Codecov:

- Minimum coverage threshold: 80%
- HTML reports generated in `htmlcov/`
- XML reports for CI integration

## Writing Tests

### Test Fixtures

Use shared fixtures from `conftest.py`:

```python
def test_with_temp_dir(temp_dir):
    """Test using temporary directory."""
    config_file = temp_dir / "config.yaml"
    # ... test implementation

def test_with_sample_config(sample_config):
    """Test using sample configuration."""
    av = AutoVision(config=sample_config)
    # ... test implementation
```

### Test Markers

Mark tests appropriately:

```python
@pytest.mark.unit
def test_fast_unit_test():
    """Fast unit test."""
    pass

@pytest.mark.integration
def test_integration():
    """Integration test."""
    pass

@pytest.mark.slow
def test_slow_operation():
    """Slow test that takes time."""
    pass
```

### Mock Dependencies

Use mocks for external dependencies:

```python
from unittest.mock import patch, Mock

@patch('autovision.youtube.YoutubeClient')
def test_youtube_integration(mock_client):
    """Test YouTube integration with mocked client."""
    mock_client.return_value.get_video.return_value = {"id": "test"}
    # ... test implementation
```

## Test Configuration

### pytest.ini Options

Key pytest configuration in `pyproject.toml`:

```toml
[tool.pytest.ini_options]
addopts = [
    "--strict-markers",
    "--cov=autovision",
    "--cov-fail-under=80",
    "-ra"
]
markers = [
    "unit: unit tests",
    "integration: integration tests",
    "slow: slow tests"
]
```

### Coverage Settings

Coverage configuration excludes:
- Test files
- Scripts
- Development utilities
- Abstract methods and protocols

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure project is installed in development mode
   ```bash
   uv pip install -e .
   ```

2. **Missing Dependencies**: Install test dependencies
   ```bash
   make install
   ```

3. **Slow Tests**: Run only fast tests during development
   ```bash
   pytest tests/ -m "unit"
   ```

### Debug Mode

Run tests with verbose output and no capture:

```bash
pytest tests/ -v -s --tb=long
```

### Test Isolation

Each test runs in isolation with temporary directories and mocked external services to ensure reproducibility and avoid side effects.
