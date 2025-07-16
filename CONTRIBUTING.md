# Contributing to AutoVision 🤝

Thank you for your interest in contributing to AutoVision! This guide will help you get started with contributing to our automated video analysis platform.

## 🎯 How to Contribute

### Types of Contributions

We welcome several types of contributions:

- 🐛 **Bug Reports**: Found a bug? Let us know!
- ✨ **Feature Requests**: Have an idea for improvement? Share it!
- 💻 **Code Contributions**: Fix bugs, implement features, improve performance
- 📝 **Documentation**: Improve docs, tutorials, examples
- 🧪 **Testing**: Add test cases, improve test coverage
- 🎨 **Design**: UI/UX improvements for Streamlit interface

## 🚀 Getting Started

### Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/your-username/AutoVision.git
   cd AutoVision
   ```

2. **Set Up Development Environment**
   ```bash
   # Using uv (recommended)
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -e ".[dev,ml]"

   # Or using pip
   python -m venv .venv
   source .venv/bin/activate
   pip install -e ".[dev,ml]"
   ```

3. **Install Pre-commit Hooks**
   ```bash
   pre-commit install
   ```

4. **Verify Setup**
   ```bash
   pytest
   python -m autovision --help
   ```

### Development Workflow

1. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/bug-description
   ```

2. **Make Your Changes**
   - Write code following our style guidelines
   - Add tests for new functionality
   - Update documentation as needed

3. **Test Your Changes**
   ```bash
   # Run tests
   pytest

   # Run linting
   ruff check src/ tests/
   ruff format src/ tests/

   # Type checking
   mypy src/
   ```

4. **Commit and Push**
   ```bash
   git add .
   git commit -m "feat: add new feature description"
   git push origin feature/your-feature-name
   ```

5. **Create Pull Request**
   - Open a PR from your fork to the main repository
   - Fill out the PR template completely
   - Link any related issues

## 📋 Development Standards

### Code Style

We use the following tools for code quality:

- **Ruff**: Fast Python linter and formatter
- **MyPy**: Static type checking
- **Black**: Code formatting (via ruff)
- **Pre-commit**: Automated checks before commits

#### Style Guidelines

```python
# Type hints are required for all functions
def process_video(url: str, config: Config) -> VideoResults:
    """Process a single video with the given configuration.

    Args:
        url: YouTube video URL
        config: Processing configuration

    Returns:
        Video processing results with predictions

    Raises:
        VideoNotFoundError: When video cannot be accessed
        ModelLoadError: When model loading fails
    """
    pass

# Use descriptive variable names
detection_results = model.predict(frame)
confidence_threshold = config.models.confidence_threshold

# Document complex logic
# Extract keyframes at regular intervals to ensure reproducible sampling
# This maintains consistency across multiple runs with the same configuration
keyframes = extract_keyframes(video, interval=config.sampling.frequency)
```

### Testing Requirements

#### Test Categories

1. **Unit Tests**: Test individual functions and classes
   ```python
   def test_config_validation():
       """Test configuration validation with invalid data."""
       with pytest.raises(ValidationError):
           Config(sampling={"frequency": -1})
   ```

2. **Integration Tests**: Test component interactions
   ```python
   def test_video_processing_pipeline():
       """Test complete video processing workflow."""
       config = Config.from_yaml("tests/fixtures/test_config.yaml")
       results = process_video("test_video_url", config)
       assert len(results.detections) > 0
   ```

3. **End-to-End Tests**: Test complete user workflows
   ```python
   def test_cli_processing():
       """Test CLI command processing."""
       result = subprocess.run([
           "python", "-m", "autovision",
           "--config", "tests/fixtures/test_config.yaml"
       ], capture_output=True)
       assert result.returncode == 0
   ```

#### Test Coverage

- Maintain **90%+ code coverage**
- All new features must include tests
- Bug fixes must include regression tests
- Use fixtures for common test data

```bash
# Run tests with coverage
pytest --cov=src/autovision --cov-report=html

# View coverage report
open htmlcov/index.html
```

### Documentation

#### Docstring Format

We use Google-style docstrings:

```python
def ensemble_predictions(predictions: List[Prediction], method: str = "voting") -> Prediction:
    """Combine multiple model predictions using ensemble methods.

    This function implements various ensemble techniques to combine predictions
    from multiple computer vision models, improving overall accuracy and
    providing confidence estimates.

    Args:
        predictions: List of predictions from different models
        method: Ensemble method to use. Options:
            - "voting": Simple majority voting
            - "weighted": Confidence-weighted voting
            - "nms": Non-maximum suppression across models

    Returns:
        Combined prediction with ensemble confidence scores

    Raises:
        ValueError: If method is not supported
        InsufficientDataError: If fewer than 2 predictions provided

    Example:
        ```python
        model1_pred = model1.predict(image)
        model2_pred = model2.predict(image)
        ensemble_result = ensemble_predictions([model1_pred, model2_pred])
        ```
    """
```

## 🐛 Bug Reports

### Before Reporting

1. **Search existing issues** for duplicates
2. **Update to latest version** and test again
3. **Check documentation** for known limitations

### Bug Report Template

```markdown
**Bug Description**
Clear description of the bug

**Steps to Reproduce**
1. Step one
2. Step two
3. See error

**Expected Behavior**
What you expected to happen

**Actual Behavior**
What actually happened

**Environment**
- OS: [e.g., Ubuntu 22.04]
- Python version: [e.g., 3.11.5]
- AutoVision version: [e.g., 0.1.0]
- GPU: [e.g., NVIDIA RTX 4090, or "None"]

**Configuration**
```yaml
# Include relevant config.yaml sections
```

**Error Output**
```
Include full error traceback
```

**Additional Context**
Any other relevant information
```

## ✨ Feature Requests

### Feature Request Template

```markdown
**Feature Description**
Clear description of the proposed feature

**Problem Statement**
What problem does this solve?

**Proposed Solution**
How would you like it implemented?

**Alternatives Considered**
Other solutions you've considered

**Implementation Ideas**
Technical implementation suggestions (optional)

**Use Cases**
Specific examples of how this would be used
```

## 🏗️ Architecture Guidelines

### Project Structure

```
src/autovision/
├── __init__.py          # Package initialization
├── cli.py              # Command-line interface
├── core.py             # Core processing logic
├── config/             # Configuration management
├── models/             # Model integration
├── video/              # Video processing
├── ensemble/           # Ensemble methods
├── export/             # Output formatting
└── gui/                # Streamlit interface

tests/
├── unit/               # Unit tests
├── integration/        # Integration tests
├── e2e/                # End-to-end tests
└── fixtures/           # Test data and configs
```

### Design Principles

1. **Modularity**: Each component should be independently testable
2. **Extensibility**: Easy to add new models, formats, ensemble methods
3. **Error Handling**: Graceful degradation and informative error messages
4. **Performance**: Efficient memory usage and processing speed
5. **Reproducibility**: Deterministic results with same configuration

### Adding New Features

#### New Model Integration

```python
# src/autovision/models/new_model.py
from .base import BaseModel

class NewModel(BaseModel):
    """Integration for new computer vision model."""

    def __init__(self, model_name: str, **kwargs):
        super().__init__(model_name, **kwargs)

    def load_model(self) -> None:
        """Load the model from source."""
        pass

    def predict(self, image: np.ndarray) -> Prediction:
        """Run inference on a single image."""
        pass
```

#### New Export Format

```python
# src/autovision/export/new_format.py
from .base import BaseExporter

class NewFormatExporter(BaseExporter):
    """Export predictions to new format."""

    def export(self, predictions: List[Prediction], output_path: str) -> None:
        """Export predictions to file."""
        pass
```

## 🔄 Pull Request Process

### PR Checklist

- [ ] **Code Quality**
  - [ ] Follows style guidelines (ruff, mypy pass)
  - [ ] Includes comprehensive tests
  - [ ] Maintains or improves code coverage
  - [ ] Updates documentation

- [ ] **Functionality**
  - [ ] Feature works as described
  - [ ] Doesn't break existing functionality
  - [ ] Includes error handling
  - [ ] Performance impact considered

- [ ] **Documentation**
  - [ ] README updated if needed
  - [ ] Docstrings added/updated
  - [ ] Configuration examples updated
  - [ ] CHANGELOG entry added

### PR Title Format

Use conventional commits format:

- `feat: add ensemble uncertainty quantification`
- `fix: resolve YouTube URL validation bug`
- `docs: update installation instructions`
- `test: add integration tests for CLI`
- `refactor: improve model loading performance`

### Review Process

1. **Automated Checks**: All CI checks must pass
2. **Code Review**: At least one maintainer review required
3. **Testing**: Manual testing of new features
4. **Documentation**: Documentation review for user-facing changes

## 🎖️ Recognition

Contributors are recognized in several ways:

- Listed in `CONTRIBUTORS.md`
- Mentioned in release notes
- Special thanks in documentation
- Invitation to maintainer team for significant contributions

## 📞 Getting Help

- **GitHub Discussions**: General questions and ideas
- **GitHub Issues**: Bug reports and feature requests
- **Discord**: Real-time chat with maintainers and community
- **Email**: team@autovision.dev for private matters

## 📄 Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).

## 🙏 Thank You

Your contributions make AutoVision better for everyone in the computer vision community. Whether you're fixing a typo or implementing a major feature, every contribution is valued and appreciated!

---

**Happy Contributing! 🚀**
