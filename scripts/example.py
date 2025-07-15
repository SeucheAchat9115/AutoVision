#!/usr/bin/env python3
"""Example usage of AutoVision."""

import sys
from pathlib import Path

# Add src to path for development
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from autovision import AutoVision


def main():
    """Run example AutoVision workflow."""
    print("AutoVision Example")
    print("=" * 50)
    
    # Initialize AutoVision
    av = AutoVision()
    print(f"AutoVision version: {av.get_version()}")
    
    # Example configuration
    config = {
        "project": {
            "name": "Example Project",
            "output_dir": "./example_output"
        },
        "youtube": {
            "keyframe_interval": 30
        }
    }
    
    av_configured = AutoVision(config=config)
    print(f"Configured AutoVision with project: {av_configured.config['project']['name']}")
    
    # Example video processing (placeholder)
    test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    result = av_configured.process_video(test_url)
    print(f"Processing result: {result}")


if __name__ == "__main__":
    main()
