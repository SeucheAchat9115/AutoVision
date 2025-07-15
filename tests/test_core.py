"""Tests for AutoVision core functionality."""

from autovision import AutoVision


def test_autovision_init():
    """Test AutoVision initialization."""
    av = AutoVision()
    assert av is not None
    assert av.config == {}


def test_autovision_init_with_config(sample_config):
    """Test AutoVision initialization with configuration."""
    av = AutoVision(config=sample_config)
    assert av.config == sample_config


def test_autovision_get_version():
    """Test getting AutoVision version."""
    av = AutoVision()
    version = av.get_version()
    assert version == "0.1.0"


def test_autovision_process_video():
    """Test video processing placeholder."""
    av = AutoVision()
    result = av.process_video("https://www.youtube.com/watch?v=test")
    
    assert result["status"] == "placeholder"
    assert result["url"] == "https://www.youtube.com/watch?v=test"
