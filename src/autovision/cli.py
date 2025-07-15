"""Command Line Interface for AutoVision."""

import argparse
import logging
import sys
from pathlib import Path

from autovision import AutoVision, __version__


def setup_logging(verbose: bool = False) -> None:
    """Setup logging configuration.

    Args:
        verbose: Enable verbose logging
    """
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )


def create_parser() -> argparse.ArgumentParser:
    """Create and configure argument parser.

    Returns:
        Configured ArgumentParser instance
    """
    parser = argparse.ArgumentParser(
        description="AutoVision: Automated video analysis and object detection"
    )

    parser.add_argument(
        "--version", action="version", version=f"AutoVision {__version__}"
    )

    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose logging"
    )

    parser.add_argument("-c", "--config", type=Path, help="Path to configuration file")

    parser.add_argument("youtube_url", nargs="?", help="YouTube URL to process")

    return parser


def main(args: list[str] | None = None) -> int:
    """Main CLI entry point.

    Args:
        args: Command line arguments (for testing)

    Returns:
        Exit code
    """
    parser = create_parser()
    parsed_args = parser.parse_args(args)

    setup_logging(parsed_args.verbose)

    try:
        autovision = AutoVision()

        if parsed_args.youtube_url:
            result = autovision.process_video(parsed_args.youtube_url)
            print(f"Processing result: {result}")
        else:
            parser.print_help()
            return 1

    except Exception as e:
        logging.error(f"Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
