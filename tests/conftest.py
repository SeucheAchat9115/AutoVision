"""Basic test configuration for AutoVision."""

import shutil
import tempfile
from collections.abc import Generator
from pathlib import Path

import pytest


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for tests."""
    temp_path = Path(tempfile.mkdtemp())
    try:
        yield temp_path
    finally:
        shutil.rmtree(temp_path, ignore_errors=True)


@pytest.fixture
def sample_config() -> dict:
    """Provide a sample configuration for testing."""
    return {
        "project": {"name": "Test Project", "output_dir": "./test_output"},
        "youtube": {"keyframe_interval": 30},
        "models": {
            "object_detection": [{"name": "test_model", "confidence_threshold": 0.5}]
        },
    }
