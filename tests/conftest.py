"""Basic test configuration for AutoVision."""

import shutil
import tempfile
from collections.abc import Generator
from pathlib import Path
from typing import Any
from unittest.mock import Mock

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
def sample_config() -> dict[str, Any]:
    """Provide a sample configuration for testing."""
    return {
        "project": {"name": "Test Project", "output_dir": "./test_output"},
        "youtube": {"keyframe_interval": 30},
        "models": {
            "object_detection": [{"name": "test_model", "confidence_threshold": 0.5}]
        },
    }


@pytest.fixture
def mock_youtube_video() -> dict[str, Any]:
    """Mock YouTube video metadata for testing."""
    return {
        "id": "test_video_id",
        "title": "Test Video",
        "duration": 120,
        "url": "https://www.youtube.com/watch?v=test_video_id",
        "thumbnail": "https://example.com/thumbnail.jpg",
    }


@pytest.fixture
def mock_model() -> Mock:
    """Mock ML model for testing."""
    model = Mock()
    model.predict.return_value = [
        {
            "bbox": [10, 10, 50, 50],
            "confidence": 0.85,
            "class": "person",
            "class_id": 0,
        }
    ]
    return model


@pytest.fixture
def sample_frame_data() -> dict[str, Any]:
    """Sample frame data for testing."""
    return {
        "timestamp": 30.0,
        "frame_number": 900,
        "width": 1920,
        "height": 1080,
        "format": "RGB",
    }
