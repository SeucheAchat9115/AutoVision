"""Tests for AutoVision core functionality."""

import pytest

from autovision import AutoVision


@pytest.mark.unit
def test_autovision_init():
    """Test AutoVision initialization."""
    av = AutoVision()
    assert av is not None
    assert av.config == {}


@pytest.mark.unit
def test_autovision_init_with_config(sample_config):
    """Test AutoVision initialization with configuration."""
    av = AutoVision(config=sample_config)
    assert av.config == sample_config


@pytest.mark.unit
def test_autovision_get_version():
    """Test getting AutoVision version."""
    av = AutoVision()
    version = av.get_version()
    assert version == "0.1.0"


@pytest.mark.unit
def test_autovision_process_video():
    """Test video processing placeholder."""
    av = AutoVision()
    result = av.process_video("https://www.youtube.com/watch?v=test")

    assert result["status"] == "placeholder"
    assert result["url"] == "https://www.youtube.com/watch?v=test"


@pytest.mark.unit
def test_autovision_config_validation(sample_config):
    """Test configuration validation."""
    av = AutoVision(config=sample_config)

    # Test that required keys are present
    assert "project" in av.config
    assert "youtube" in av.config
    assert "models" in av.config

    # Test project configuration
    assert av.config["project"]["name"] == "Test Project"
    assert av.config["project"]["output_dir"] == "./test_output"


@pytest.mark.unit
def test_autovision_invalid_config():
    """Test handling of invalid configuration."""
    invalid_config = {"invalid": "config"}
    av = AutoVision(config=invalid_config)

    # Should accept any config but not crash
    assert av.config == invalid_config


@pytest.mark.unit
def test_autovision_empty_process_video():
    """Test processing empty video URL."""
    av = AutoVision()
    result = av.process_video("")

    assert result["status"] == "placeholder"
    assert result["url"] == ""


@pytest.mark.slow
@pytest.mark.integration
def test_autovision_full_pipeline_mock():
    """Test full pipeline with mocked components."""
    config = {
        "project": {"name": "Integration Test", "output_dir": "./test_output"},
        "youtube": {"keyframe_interval": 10},
        "models": {"object_detection": [{"name": "mock_model"}]},
    }

    av = AutoVision(config=config)

    # This would be a more comprehensive test in a real implementation
    # For now, just test that initialization works with complex config
    assert av.config["youtube"]["keyframe_interval"] == 10
    assert len(av.config["models"]["object_detection"]) == 1
