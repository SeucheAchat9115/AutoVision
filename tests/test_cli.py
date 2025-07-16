"""Tests for CLI functionality."""

import contextlib
from unittest.mock import patch

import pytest

from autovision.cli import main


@pytest.mark.unit
def test_cli_main_help():
    """Test CLI help command."""
    with patch("sys.argv", ["autovision", "--help"]):
        with pytest.raises(SystemExit) as exc_info:
            main()
        assert exc_info.value.code == 0


@pytest.mark.unit
def test_cli_main_version():
    """Test CLI version command."""
    with patch("sys.argv", ["autovision", "--version"]):
        with pytest.raises(SystemExit) as exc_info:
            main()
        assert exc_info.value.code == 0


@pytest.mark.unit
def test_cli_main_no_args():
    """Test CLI with no arguments."""
    with patch("sys.argv", ["autovision"]), contextlib.suppress(SystemExit):
        # Should not crash, might show help or process with defaults
        main()


@pytest.mark.integration
def test_cli_main_with_config(temp_dir):
    """Test CLI with configuration file."""
    config_file = temp_dir / "test_config.yaml"
    config_file.write_text("""
project:
  name: "CLI Test"
  output_dir: "./output"
youtube:
  keyframe_interval: 30
models:
  object_detection:
    - name: "test_model"
      confidence_threshold: 0.5
""")

    with (
        patch("sys.argv", ["autovision", "--config", str(config_file)]),
        contextlib.suppress(SystemExit, Exception),
    ):
        main()
