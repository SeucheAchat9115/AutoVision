Stage 1: Core MVP & Foundational Setup 📦

Development & Environment
	1.	Project Initialization
	•	PR: Setup project repository with uv venv and .gitignore.
	2.	Code Quality & Pre-commits
	•	PR: Add pre-commit configuration with ruff.
	•	PR: Integrate mypy for static type checking.
	3.	Testing Framework
	•	PR: Setup pytest and basic test folder structure.

Key Features
	4.	Batch Data Input
	•	PR: Implement parsing YouTube URLs from a config file (config.yaml).
	5.	CLI with Argparse
	•	PR: Add argparse-based CLI accepting --config path.
	6.	Hugging Face Model Integration
	•	PR: Integrate model loading from Hugging Face (object detection only).
	7.	Keyframe Extraction
	•	PR: Implement timestamp-based keyframe extraction (configurable frequency).
	8.	Configuration File
	•	PR: Define config.yaml schema and loader with validation.
	9.	Output Format
	•	PR: Implement COCO JSON writer including predictions + timestamp metadata.
	10.	Error Handling
	•	PR: Centralized error handling for:
	•	YouTube API errors
	•	Video unavailability
	•	Model inference failure

Testing
	11.	Unit Tests
	•	PR: Unit tests for keyframe extraction reproducibility.
	12.	Integration Tests
	•	PR: Model loading and inference integration tests.
	13.	CLI Interface Testing
	•	PR: CLI execution test with dummy config and dry run.

⸻

Stage 2: Interactive App & Model Expansion 🖥️

Development & CI Pipeline
	14.	Continuous Integration (CI)
	•	PR: GitHub Actions for tests, linting, typing checks.
	15.	Enhanced Testing
	•	PR: Expand test coverage for planned GUI and multi-task support.

Key Features
	16.	GUI with Streamlit
	•	PR: Basic Streamlit app scaffolding to trigger core pipeline.
	17.	Configuration Management
	•	PR: Implement load, display, edit, and export of config.yaml via UI.
	18.	Multi-Task Support
	•	PR: Add semantic segmentation model support.
	19.	Label Visualization
	•	PR: Display frames with prediction overlays in GUI.
	20.	Model Switching
	•	PR: Implement model selection dropdown for different Hugging Face models.
	21.	Export Format Options
	•	PR: Enable export in COCO, YOLO, Pascal VOC, and custom formats.

Testing
	22.	Streamlit Component Tests
	•	PR: Test Streamlit workflows and UI elements.
	23.	Config File Validation Tests
	•	PR: Validate integrity and completeness of config files.
	24.	Multi-format Export Tests
	•	PR: Validate each export format produces correct outputs.
	25.	Multi-task Model Inference Testing
	•	PR: Test object detection vs. segmentation model outputs.

⸻

Stage 3: Model Ensemble & Public Packaging ✍️

Packaging & CD
	26.	Automatic PyPI Deployment
	•	PR: CD pipeline for PyPI deployment on tagged releases.
	27.	Package Distribution
	•	PR: Ensure pip-installable autovision-tool with entry points.

Key Features
	28.	Multi-Model Ensemble
	•	PR: Implement inference with multiple models in parallel.
	29.	Model Agreement Analysis
	•	PR: Compute agreement scores across models’ predictions.
	30.	Fine-tuned Model Support
	•	PR: Enable loading custom fine-tuned models.
	31.	Advanced Configuration
	•	PR: Support model-specific parameters and ensemble weights in config.
	32.	Export Versioning
	•	PR: Auto-increment output versioning (export_v3.json).
	33.	Confidence Scoring
	•	PR: Add confidence scores per prediction.

Testing
	34.	Ensemble Prediction Tests
	•	PR: Validate ensemble inference accuracy.
	35.	Model Agreement Validation
	•	PR: Unit tests for agreement metrics.
	36.	Fine-tuned Model Tests
	•	PR: Test inference with custom models.
	37.	Installation/Distribution Tests
	•	PR: Verify correct pip install, CLI entry points, and minimal examples.

⸻

Stage 4: Advanced Ensemble Platform & Deployment 🌐

Deployment
	38.	Containerization
	•	PR: Dockerize complete app including GUI + backend.
	39.	Streamlit Cloud Deployment
	•	PR: Deploy to Streamlit Cloud, with instructions.

Key Features
	40.	Voting-based Consensus Methods
	•	PR: Majority voting, weighted voting, confidence-based methods.
	41.	Non-Maximum Suppression (NMS) Across Models
	•	PR: Implement NMS across ensemble outputs.
	42.	Ensemble Uncertainty Quantification
	•	PR: Compute uncertainty metrics from ensemble predictions.
	43.	Model Performance Dashboard
	•	PR: Add Streamlit dashboard for per-model metrics and visualizations.
	44.	Batch Processing Interface
	•	PR: GUI component for batch processing + progress bar.
	45.	Advanced Export Options
	•	PR: Export ensemble predictions, individual model outputs, uncertainty maps.
	46.	Custom Model Integration
	•	PR: GUI + backend to upload and use custom-trained models.

Database Schema
	47.	Database: Projects Table
	•	PR: Implement Projects schema.
	48.	Database: Models Table
	•	PR: Implement Models registry with metadata.
	49.	Database: Predictions Table
	•	PR: Implement storage of predictions with confidence.
	50.	Database: Ensembles Table
	•	PR: Store merged predictions and agreement.
	51.	Database: Frames Table
	•	PR: Store metadata for URL + timestamps.

Testing
	52.	Ensemble Algorithm Performance
	•	PR: Tests for ensemble methods, NMS, uncertainty.
	53.	Model Performance Tracking
	•	PR: Tests to validate metrics computation per model.
	54.	Batch Processing Workflow Tests
	•	PR: Validate correctness of batch processing.
	55.	Custom Model Upload Tests
	•	PR: Tests for uploading and running custom models.