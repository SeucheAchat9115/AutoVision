"""Tests for configuration functionality."""

from pathlib import Path

import pytest
import yaml


@pytest.mark.unit
def test_config_file_creation(temp_dir: Path) -> None:
    """Test creating a configuration file."""
    config_file = temp_dir / "config.yaml"

    config_data = {
        "project": {"name": "Test", "output_dir": "./output"},
        "youtube": {"keyframe_interval": 30},
        "models": {"object_detection": [{"name": "test_model"}]},
    }

    with open(config_file, "w") as f:
        yaml.dump(config_data, f)

    assert config_file.exists()

    # Read back and verify
    with open(config_file) as f:
        loaded_config = yaml.safe_load(f)

    assert loaded_config == config_data


@pytest.mark.unit
def test_invalid_yaml_config(temp_dir: Path) -> None:
    """Test handling of invalid YAML configuration."""
    config_file = temp_dir / "invalid_config.yaml"

    # Write invalid YAML
    config_file.write_text("invalid: yaml: content: [")

    with pytest.raises(yaml.YAMLError), open(config_file) as f:
        yaml.safe_load(f)


@pytest.mark.unit
def test_empty_config_file(temp_dir: Path) -> None:
    """Test handling of empty configuration file."""
    config_file = temp_dir / "empty_config.yaml"
    config_file.write_text("")

    with open(config_file) as f:
        loaded_config = yaml.safe_load(f)

    assert loaded_config is None


@pytest.mark.unit
def test_config_with_comments(temp_dir: Path) -> None:
    """Test configuration file with comments."""
    config_file = temp_dir / "commented_config.yaml"

    config_content = """
# AutoVision Configuration
project:
  name: "Test Project"  # Project name
  output_dir: "./output"  # Output directory

# YouTube settings
youtube:
  keyframe_interval: 30  # Seconds between keyframes

# Model configuration
models:
  object_detection:
    - name: "test_model"  # Model name
      confidence_threshold: 0.5  # Minimum confidence
"""

    config_file.write_text(config_content)

    with open(config_file) as f:
        loaded_config = yaml.safe_load(f)

    assert loaded_config["project"]["name"] == "Test Project"
    assert loaded_config["youtube"]["keyframe_interval"] == 30
    assert len(loaded_config["models"]["object_detection"]) == 1
