# AutoVision - Planned Folder Structure

This file shows the complete folder structure for AutoVision after implementing all planned features from the four-phase development plan.

## 📁 Complete Project Structure

```
AutoVision/
├── .github/                          # GitHub Workflows and Templates
│   ├── workflows/
│   │   ├── ci.yml                    # Continuous Integration
│   │   ├── cd.yml                    # Continuous Deployment
│   │   ├── security.yml              # Security Scans
│   │   └── release.yml               # Release Automation
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   └── question.md
│   └── pull_request_template.md
│
├── .claude/                          # Claude AI Project Documentation
│   ├── prd.md                        # Product Requirements Document
│   ├── implementation_plan.md         # Detailed Implementation Plan
│   ├── project_plan.md              # Project Overview
│   └── folder_structure.md           # This file
│
├── config/                           # Configuration Files and Templates
│   ├── default.yaml                  # Default Configuration
│   ├── example_detection.yaml        # Example for Object Detection
│   ├── example_segmentation.yaml     # Example for Segmentation
│   ├── example_ensemble.yaml         # Example for Ensemble Configuration
│   ├── presets/                      # Predefined Configuration Profiles
│   │   ├── fast_detection.yaml       # Fast Detection
│   │   ├── accurate_detection.yaml   # Accurate Detection
│   │   ├── multi_task.yaml          # Multi-Task Configuration
│   │   └── enterprise.yaml          # Enterprise Configuration
│   └── schema/
│       └── config_schema.json        # JSON Schema for Configuration
│
├── data/                             # Data Storage and Cache
│   ├── cache/                        # Model and Prediction Cache
│   │   ├── models/                   # Cached Models
│   │   ├── predictions/              # Cached Predictions
│   │   └── frames/                   # Temporary Keyframes
│   ├── temp/                         # Temporary Files
│   └── logs/                         # Application Logs
│
├── deployment/                       # Deployment Configurations
│   ├── docker/
│   │   ├── Dockerfile                # Container Definition
│   │   ├── docker-compose.yml        # Multi-Container Setup
│   │   ├── docker-compose.dev.yml    # Development Environment
│   │   └── .dockerignore
│   ├── kubernetes/                   # Kubernetes Manifests
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   └── ingress.yaml
│   ├── cloud/                        # Cloud-specific Configurations
│   │   ├── aws/
│   │   ├── gcp/
│   │   └── azure/
│   └── scripts/
│       ├── deploy.sh                 # Deployment Script
│       └── setup.sh                  # Setup Script
│
├── docs/                             # Project Documentation
│   ├── api/                          # API Documentation
│   │   ├── rest_api.md
│   │   └── python_api.md
│   ├── user_guide/                   # User Manual
│   │   ├── installation.md
│   │   ├── quick_start.md
│   │   ├── configuration.md
│   │   ├── gui_usage.md
│   │   └── cli_usage.md
│   ├── developer_guide/              # Developer Manual
│   │   ├── architecture.md
│   │   ├── contributing.md
│   │   ├── testing.md
│   │   └── model_integration.md
│   ├── tutorials/                    # Tutorials and Examples
│   │   ├── basic_detection.md
│   │   ├── ensemble_setup.md
│   │   ├── custom_models.md
│   │   └── batch_processing.md
│   ├── assets/                       # Documentation Assets
│   │   ├── images/
│   │   ├── videos/
│   │   └── diagrams/
│   └── TESTING.md
│
├── scripts/                          # Utility Scripts
│   ├── example.py                    # Example Script
│   ├── benchmark.py                  # Performance Benchmarks
│   ├── migration/                    # Database Migrations
│   │   ├── init_db.py
│   │   └── migrate_v1_to_v2.py
│   ├── deployment/                   # Deployment Scripts
│   │   ├── build.py
│   │   └── release.py
│   └── utils/                        # Utility Scripts
│       ├── data_cleanup.py
│       └── model_validator.py
│
├── src/                              # Main Source Code
│   └── autovision/
│       ├── __init__.py               # Package Initialization
│       ├── main.py                   # Main Entry Point
│       ├── cli.py                    # Command Line Interface
│       ├── core.py                   # Core Processing Logic
│       │
│       ├── api/                      # REST API Module
│       │   ├── __init__.py
│       │   ├── app.py                # FastAPI Application
│       │   ├── routes/               # API Routes
│       │   │   ├── __init__.py
│       │   │   ├── videos.py         # Video Processing Endpoints
│       │   │   ├── models.py         # Model Management Endpoints
│       │   │   ├── projects.py       # Project Management Endpoints
│       │   │   └── auth.py           # Authentication Endpoints
│       │   ├── middleware/           # API Middleware
│       │   │   ├── __init__.py
│       │   │   ├── auth.py
│       │   │   ├── rate_limiting.py
│       │   │   └── logging.py
│       │   └── schemas/              # Pydantic Schemas
│       │       ├── __init__.py
│       │       ├── video.py
│       │       ├── model.py
│       │       └── project.py
│       │
│       ├── config/                   # Configuration Management
│       │   ├── __init__.py
│       │   ├── loader.py             # YAML Config Loader
│       │   ├── validator.py          # Config Validation
│       │   ├── schema.py             # Pydantic Models
│       │   └── defaults.py           # Default Settings
│       │
│       ├── database/                 # Database Integration
│       │   ├── __init__.py
│       │   ├── connection.py         # Database Connection
│       │   ├── models.py             # SQLAlchemy Models
│       │   ├── migrations/           # Database Migrations
│       │   │   ├── __init__.py
│       │   │   └── versions/
│       │   └── repositories/         # Data Access Layer
│       │       ├── __init__.py
│       │       ├── project.py
│       │       ├── model.py
│       │       └── prediction.py
│       │
│       ├── ensemble/                 # Ensemble Methods
│       │   ├── __init__.py
│       │   ├── base.py               # Base Ensemble Class
│       │   ├── voting.py             # Voting-based Ensembles
│       │   ├── weighted.py           # Weighted Ensembles
│       │   ├── confidence.py         # Confidence-based Ensembles
│       │   ├── nms.py                # Non-Maximum Suppression
│       │   ├── uncertainty.py        # Uncertainty Quantification
│       │   └── optimization.py       # Ensemble Optimization
│       │
│       ├── export/                   # Export Functionality
│       │   ├── __init__.py
│       │   ├── base.py               # Base Exporter
│       │   ├── coco.py               # COCO Format Export
│       │   ├── yolo.py               # YOLO Format Export
│       │   ├── pascal_voc.py         # Pascal VOC Format Export
│       │   ├── custom.py             # Custom Format Export
│       │   ├── ensemble.py           # Ensemble-specific Exports
│       │   ├── visualization.py      # Visualization Exports
│       │   └── metadata.py           # Metadata Export
│       │
│       ├── gui/                      # Streamlit GUI
│       │   ├── __init__.py
│       │   ├── app.py                # Main GUI Application
│       │   ├── pages/                # GUI Pages
│       │   │   ├── __init__.py
│       │   │   ├── home.py           # Homepage
│       │   │   ├── configuration.py  # Configuration Page
│       │   │   ├── processing.py     # Processing Page
│       │   │   ├── visualization.py  # Visualization Page
│       │   │   ├── models.py         # Model Management
│       │   │   ├── ensemble.py       # Ensemble Configuration
│       │   │   ├── dashboard.py      # Performance Dashboard
│       │   │   └── export.py         # Export Page
│       │   ├── components/           # Reusable Components
│       │   │   ├── __init__.py
│       │   │   ├── config_editor.py  # Configuration Editor
│       │   │   ├── model_selector.py # Model Selection
│       │   │   ├── progress_bar.py   # Progress Indicator
│       │   │   ├── visualization.py  # Visualization Components
│       │   │   └── file_uploader.py  # File Upload
│       │   └── utils/                # GUI Utilities
│       │       ├── __init__.py
│       │       ├── session.py        # Session Management
│       │       ├── styling.py        # UI Styling
│       │       └── validation.py     # Input Validation
│       │
│       ├── models/                   # Model Integration
│       │   ├── __init__.py
│       │   ├── base.py               # Base Model Interface
│       │   ├── registry.py           # Model Registry
│       │   ├── loader.py             # Model Loader
│       │   ├── cache.py              # Model Caching
│       │   ├── huggingface/          # Hugging Face Integration
│       │   │   ├── __init__.py
│       │   │   ├── detector.py       # Object Detection Models
│       │   │   ├── segmenter.py      # Segmentation Models
│       │   │   ├── transformer.py    # Transformer Models
│       │   │   └── downloader.py     # Model Download Management
│       │   ├── custom/               # Custom Model Integration
│       │   │   ├── __init__.py
│       │   │   ├── validator.py      # Custom Model Validation
│       │   │   ├── converter.py      # Model Format Conversion
│       │   │   └── wrapper.py        # Custom Model Wrapper
│       │   ├── inference/            # Inference Engine
│       │   │   ├── __init__.py
│       │   │   ├── batch.py          # Batch Processing
│       │   │   ├── parallel.py       # Parallel Processing
│       │   │   └── optimization.py   # Inference Optimization
│       │   └── metadata/             # Model Metadata
│       │       ├── __init__.py
│       │       ├── performance.py    # Performance Tracking
│       │       └── versioning.py     # Model Versioning
│       │
│       ├── processing/               # Core Processing
│       │   ├── __init__.py
│       │   ├── pipeline.py           # Processing Pipeline
│       │   ├── keyframes.py          # Keyframe Extraction
│       │   ├── batch.py              # Batch Processing
│       │   ├── parallel.py           # Parallel Processing
│       │   ├── monitoring.py         # Progress Monitoring
│       │   └── optimization.py       # Performance Optimization
│       │
│       ├── utils/                    # Utility Modules
│       │   ├── __init__.py
│       │   ├── logging.py            # Logging Configuration
│       │   ├── errors.py             # Error Handling
│       │   ├── validation.py         # Input Validation
│       │   ├── file_utils.py         # File Utilities
│       │   ├── image_utils.py        # Image Utilities
│       │   ├── time_utils.py         # Time Utilities
│       │   └── system_utils.py       # System Utilities
│       │
│       ├── video/                    # Video Processing
│       │   ├── __init__.py
│       │   ├── youtube.py            # YouTube Integration
│       │   ├── downloader.py         # Video Download
│       │   ├── extractor.py          # Keyframe Extraction
│       │   ├── processor.py          # Video Processing
│       │   ├── metadata.py           # Video Metadata
│       │   └── validation.py         # Video Validation
│       │
│       └── visualization/            # Visualization
│           ├── __init__.py
│           ├── overlays.py           # Prediction Overlays
│           ├── plots.py              # Performance Plots
│           ├── dashboard.py          # Dashboard Visualizations
│           ├── ensemble.py           # Ensemble Visualizations
│           ├── confidence.py         # Confidence Visualizations
│           └── export.py             # Visualization Export
│
├── tests/                            # Test Suite
│   ├── __init__.py
│   ├── conftest.py                   # Pytest Configuration
│   ├── fixtures/                     # Test Fixtures
│   │   ├── __init__.py
│   │   ├── config_files/             # Test Configuration Files
│   │   ├── sample_videos/            # Sample Video URLs
│   │   ├── mock_models/              # Mock Model Responses
│   │   └── expected_outputs/         # Expected Test Outputs
│   │
│   ├── unit/                         # Unit Tests
│   │   ├── __init__.py
│   │   ├── test_config.py            # Configuration Tests
│   │   ├── test_core.py              # Core Logic Tests
│   │   ├── test_cli.py               # CLI Tests
│   │   ├── test_models/              # Model Tests
│   │   │   ├── __init__.py
│   │   │   ├── test_loader.py
│   │   │   ├── test_registry.py
│   │   │   └── test_inference.py
│   │   ├── test_ensemble/            # Ensemble Tests
│   │   │   ├── __init__.py
│   │   │   ├── test_voting.py
│   │   │   ├── test_weighted.py
│   │   │   └── test_uncertainty.py
│   │   ├── test_export/              # Export Tests
│   │   │   ├── __init__.py
│   │   │   ├── test_coco.py
│   │   │   ├── test_yolo.py
│   │   │   └── test_custom.py
│   │   ├── test_video/               # Video Processing Tests
│   │   │   ├── __init__.py
│   │   │   ├── test_youtube.py
│   │   │   └── test_extractor.py
│   │   └── test_utils/               # Utility Tests
│   │       ├── __init__.py
│   │       ├── test_logging.py
│   │       └── test_validation.py
│   │
│   ├── integration/                  # Integration Tests
│   │   ├── __init__.py
│   │   ├── test_end_to_end.py        # Complete Workflow Tests
│   │   ├── test_cli_integration.py   # CLI Integration Tests
│   │   ├── test_gui_integration.py   # GUI Integration Tests
│   │   ├── test_api_integration.py   # API Integration Tests
│   │   ├── test_model_integration.py # Model Integration Tests
│   │   └── test_ensemble_workflow.py # Ensemble Workflow Tests
│   │
│   ├── performance/                  # Performance Tests
│   │   ├── __init__.py
│   │   ├── test_benchmarks.py        # Performance Benchmarks
│   │   ├── test_memory_usage.py      # Memory Usage Tests
│   │   └── test_scalability.py       # Scalability Tests
│   │
│   └── e2e/                          # End-to-End Tests
│       ├── __init__.py
│       ├── test_complete_pipeline.py # Complete Pipeline Tests
│       ├── test_gui_workflows.py     # GUI Workflow Tests
│       └── test_api_workflows.py     # API Workflow Tests
│
├── .gitignore                        # Git Ignore Rules
├── .pre-commit-config.yaml           # Pre-commit Hooks
├── .ruff.toml                        # Ruff Configuration
├── CONTRIBUTING.md                   # Contributing Guide
├── coverage.xml                      # Coverage Report
├── LICENSE                           # MIT License
├── main.py                           # Legacy Entry Point
├── Makefile                          # Build Commands
├── pyproject.toml                    # Python Project Configuration
├── README.md                         # Project README
├── requirements.txt                  # Python Dependencies (Legacy)
├── requirements-dev.txt              # Development Dependencies
├── tox.ini                           # Tox Test Configuration
└── uv.lock                           # UV Lock File
```

## 📝 Description of Main Modules

### 🎯 Core Modules (`src/autovision/`)

- **`cli.py`**: Extended Command-Line Interface with all features
- **`core.py`**: Central processing logic and orchestration
- **`main.py`**: Main entry point for all interfaces

### 🤖 Model Management (`src/autovision/models/`)

- **Hugging Face Integration**: Automatic model download and caching
- **Custom Model Support**: Integration of user-defined models
- **Model Registry**: Central management of all available models
- **Performance Tracking**: Model performance monitoring

### 🎮 Ensemble System (`src/autovision/ensemble/`)

- **Voting Methods**: Majority, weighted, confidence-based voting
- **Non-Maximum Suppression**: Cross-model NMS for better results
- **Uncertainty Quantification**: Uncertainty estimation for predictions
- **Optimization**: Automatic ensemble optimization

### 🖥️ User Interfaces

- **CLI**: Complete Command-Line Interface for automation
- **Streamlit GUI**: Interactive web user interface
- **REST API**: Programmatic access for enterprise integration

### 📊 Export & Visualization

- **Multiple Formats**: COCO, YOLO, Pascal VOC, Custom JSON
- **Ensemble Exports**: Special formats for ensemble results
- **Visualizations**: Overlays, dashboards, performance plots

### 🗄️ Database Integration

- **PostgreSQL**: Metadata, predictions, performance metrics
- **Model Registry**: Persistent model management
- **Project Management**: Project-based organization

### 🚀 Deployment & Operations

- **Docker Containerization**: Complete container solution
- **Kubernetes Support**: Scalable cloud deployment
- **CI/CD Pipeline**: Automated testing and deployment

## 🔄 Development Phases

This structure will be developed in 4 phases:

1. **Phase 1** (6-8 weeks): Core MVP with CLI and basic functionality
2. **Phase 2** (8-10 weeks): Streamlit GUI and extended features
3. **Phase 3** (10-12 weeks): Ensemble system and PyPI package
4. **Phase 4** (12-16 weeks): Enterprise platform and deployment

Each phase builds on the previous one and systematically extends functionality.
