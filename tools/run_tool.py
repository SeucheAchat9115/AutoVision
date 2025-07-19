#!/usr/bin/env python3
"""
AutoVision Run Tool

A command-line tool to load configuration, download YouTube videos,
and process them using AutoVision for object detection and analysis.
"""

import argparse
import logging
import sys
import yaml
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from autovision import AutoVision


@dataclass
class VideoProcessingResult:
    """Result of video processing operation."""
    url: str
    status: str
    error: str | None = None
    output_path: str | None = None


class YouTubeVideoProcessor:
    """
    YouTube video processor that integrates with AutoVision.
    
    Handles downloading and processing of YouTube videos specified in configuration.
    """
    
    def __init__(self, config: dict[str, Any], autovision: AutoVision):
        """
        Initialize the YouTube video processor.
        
        Args:
            config: Configuration dictionary containing video URLs and options
            autovision: AutoVision instance for video processing
        """
        self.config = config
        self.autovision = autovision
        self.logger = logging.getLogger(__name__)
        
    def get_video_urls(self) -> list[str]:
        """
        Extract video URLs from configuration.
        
        Returns:
            List of YouTube video URLs to process
        """
        try:
            return self.config.get("input", {}).get("youtube", {}).get("video_urls", [])
        except (KeyError, AttributeError) as e:
            self.logger.error(f"Error extracting video URLs from config: {e}")
            return []
    
    def get_download_options(self) -> dict[str, Any]:
        """
        Extract download options from configuration.
        
        Returns:
            Dictionary of download options (quality, format, etc.)
        """
        try:
            return self.config.get("input", {}).get("youtube", {}).get("download_options", {})
        except (KeyError, AttributeError) as e:
            self.logger.error(f"Error extracting download options from config: {e}")
            return {"quality": "best", "format": "mp4"}
    
    def download_video(self, url: str) -> VideoProcessingResult:
        """
        Download a single YouTube video.
        
        Args:
            url: YouTube video URL
            
        Returns:
            VideoProcessingResult with download status
        """
        self.logger.info(f"Starting download for video: {url}")
        
        try:
            # In a real implementation, you would use yt-dlp or similar
            # For now, we'll simulate the download process
            download_options = self.get_download_options()
            self.logger.info(f"Download options: {download_options}")
            
            # Simulate successful download
            output_path = f"downloads/{url.split('=')[-1]}.{download_options.get('format', 'mp4')}"
            
            return VideoProcessingResult(
                url=url,
                status="downloaded",
                output_path=output_path
            )
            
        except Exception as e:
            self.logger.error(f"Failed to download video {url}: {e}")
            return VideoProcessingResult(
                url=url,
                status="failed",
                error=str(e)
            )
    
    def process_video(self, url: str) -> VideoProcessingResult:
        """
        Process a single YouTube video using AutoVision.
        
        Args:
            url: YouTube video URL
            
        Returns:
            VideoProcessingResult with processing status
        """
        self.logger.info(f"Processing video with AutoVision: {url}")
        
        try:
            # Use AutoVision to process the video
            result = self.autovision.process_video(url)
            
            return VideoProcessingResult(
                url=url,
                status="processed",
                output_path=result.get("output_path")
            )
            
        except Exception as e:
            self.logger.error(f"Failed to process video {url}: {e}")
            return VideoProcessingResult(
                url=url,
                status="failed",
                error=str(e)
            )
    
    def process_all_videos(self) -> list[VideoProcessingResult]:
        """
        Download and process all videos specified in the configuration.
        
        Returns:
            List of VideoProcessingResult for each video
        """
        video_urls = self.get_video_urls()
        
        if not video_urls:
            self.logger.warning("No video URLs found in configuration")
            return []
        
        self.logger.info(f"Found {len(video_urls)} videos to process")
        results = []
        
        for url in video_urls:
            # First download the video
            download_result = self.download_video(url)
            
            if download_result.status == "downloaded":
                # Then process it with AutoVision
                process_result = self.process_video(url)
                results.append(process_result)
            else:
                # If download failed, add the failed result
                results.append(download_result)
        
        return results


def load_config(config_path: Path) -> dict[str, Any]:
    """
    Load configuration from YAML file.
    
    Args:
        config_path: Path to the configuration file
        
    Returns:
        Configuration dictionary
        
    Raises:
        FileNotFoundError: If config file doesn't exist
        yaml.YAMLError: If config file is invalid YAML
    """
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    try:
        with open(config_path, encoding="utf-8") as f:
            config = yaml.safe_load(f)
            
        if config is None:
            config = {}
            
        logging.info(f"Loaded configuration from {config_path}")
        return config
        
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Invalid YAML in config file {config_path}: {e}") from e


def setup_logging(verbose: bool = False) -> None:
    """
    Setup logging configuration.
    
    Args:
        verbose: Enable verbose (DEBUG) logging
    """
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )


def create_parser() -> argparse.ArgumentParser:
    """
    Create and configure argument parser.
    
    Returns:
        Configured ArgumentParser instance
    """
    parser = argparse.ArgumentParser(
        description="AutoVision Run Tool - Download and process YouTube videos",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -c config/default.yaml
  %(prog)s -c my_config.yaml --verbose
  %(prog)s -c config.yaml --dry-run
        """
    )
    
    parser.add_argument(
        "-c", "--config",
        type=Path,
        required=True,
        help="Path to configuration YAML file"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be processed without actually doing it"
    )
    
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("./output"),
        help="Output directory for processed videos (default: ./output)"
    )
    
    return parser


def main() -> int:
    """
    Main entry point for the run tool.
    
    Returns:
        Exit code (0 for success, 1 for error)
    """
    parser = create_parser()
    args = parser.parse_args()
    
    setup_logging(args.verbose)
    logger = logging.getLogger(__name__)
    
    try:
        # Load configuration
        logger.info("Loading configuration...")
        config = load_config(args.config)
        
        if args.dry_run:
            logger.info("DRY RUN MODE - No actual processing will occur")
            
        # Initialize AutoVision with config
        logger.info("Initializing AutoVision...")
        autovision = AutoVision(config=config)
        
        # Create YouTube video processor
        logger.info("Creating YouTube video processor...")
        video_processor = YouTubeVideoProcessor(config, autovision)
        
        # Get video URLs to show what will be processed
        video_urls = video_processor.get_video_urls()
        download_options = video_processor.get_download_options()
        
        logger.info(f"Found {len(video_urls)} videos to process")
        logger.info(f"Download options: {download_options}")
        
        if args.dry_run:
            logger.info("Videos that would be processed:")
            for i, url in enumerate(video_urls, 1):
                logger.info(f"  {i}. {url}")
            return 0
        
        # Create output directory
        args.output_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Output directory: {args.output_dir}")
        
        # Process all videos
        logger.info("Starting video processing...")
        results = video_processor.process_all_videos()
        
        # Report results
        logger.info("Processing complete!")
        
        success_count = sum(1 for r in results if r.status in ["downloaded", "processed"])
        failed_count = len(results) - success_count
        
        logger.info(f"Results: {success_count} successful, {failed_count} failed")
        
        for result in results:
            if result.status == "failed":
                logger.error(f"FAILED - {result.url}: {result.error}")
            else:
                logger.info(f"SUCCESS - {result.url}: {result.status}")
                if result.output_path:
                    logger.info(f"  Output: {result.output_path}")
        
        return 0 if failed_count == 0 else 1
        
    except FileNotFoundError as e:
        logger.error(f"Configuration file error: {e}")
        return 1
    except yaml.YAMLError as e:
        logger.error(f"Configuration parsing error: {e}")
        return 1
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        if args.verbose:
            logger.exception("Full traceback:")
        return 1


if __name__ == "__main__":
    sys.exit(main())