# 📦 AutoVision Project PR Plan (Restructured for CI/CD, Packaging First)

---

## 🔵 Phase 1: CI/CD, Packaging, and Deployment Foundations

### PR1: Project Initialization
- Initialize repo, set up `uv venv`, `.gitignore`, base Python package structure.
- ✅ **Test:** Project installation, `python -m autovision` dry run.

### PR2: Code Quality Setup
- Add pre-commit hooks with `ruff` for linting.
- ✅ **Test:** Lint sample files, CI fails on lint errors.

### PR3: Static Typing with `mypy`
- Integrate `mypy` in pre-commit and CI.
- ✅ **Test:** Introduce typed stub, validate type-checking via CI.

### PR4: Testing Framework Setup
- Setup `pytest` with base test structure.
- ✅ **Test:** Basic "test passes" example, CI runs `pytest` successfully.

### PR5: Initial GitHub Actions CI
- Add GitHub Actions to run: lint, mypy, pytest on PRs.
- ✅ **Test:** Deliberately failing test case to validate CI failure.

### PR6: CD Pipeline for PyPI Publishing
- Add GitHub Actions for PyPI deployment on version tags.
- ✅ **Test:** Mock release version tag, dry run PyPI packaging.

### PR7: Dockerization
- Add `Dockerfile` to containerize CLI and future app.
- ✅ **Test:** Docker build and basic CLI execution inside container.

### PR8: Streamlit Deployment Setup
- Initial dummy Streamlit app and deployment pipeline to Streamlit Cloud.
- ✅ **Test:** Confirm dummy app deploys successfully.

---

## 🔵 Phase 2: Core CLI, Inference, and Outputs

### PR9: Configuration Loader
- Load and validate `config.yaml`.
- ✅ **Test:** Valid/invalid config files, validation errors.

### PR10: Batch Data Input
- Parse and store YouTube URLs from config.
- ✅ **Test:** Config with multiple URLs parsed correctly.

### PR11: CLI with Argparse
- CLI entrypoint (`autovision --config config.yaml`).
- ✅ **Test:** CLI runs with valid config, errors on missing/invalid config.

### PR12: Hugging Face Model Integration
- Load pre-trained object detection model from Hugging Face.
- ✅ **Test:** Model loads, inference on dummy data, mock network failure.

### PR13: Keyframe Extraction
- Timestamp-based keyframe sampling with configurable frequency.
- ✅ **Test:** Deterministic outputs across runs, edge cases (empty video).

### PR14: Model Inference
- Run detection model on extracted keyframes (timestamps).
- ✅ **Test:** Inference outputs with dummy frames, failure scenarios.

### PR15: COCO JSON Output Writer
- Export predictions + timestamps into COCO JSON format.
- ✅ **Test:** Validate JSON schema correctness.

### PR16: Unified Error Handling
- Standard error handling for:
  - YouTube API limits
  - Model inference errors
  - Network issues
- ✅ **Test:** Mock errors for each scenario, ensure graceful failure.

---

## 🔵 Phase 3: Enhanced Testing & Multi-task Features

### PR17: CLI Interface Tests
- Comprehensive tests for CLI argument handling and execution paths.
- ✅ **Test:** Various CLI args, invalid paths, dry run mode.

### PR18: Semantic Segmentation Model Support
- Add Hugging Face segmentation model option.
- ✅ **Test:** Segmentation output shape, config switching between tasks.

### PR19: Export Format Options
- Add YOLO, Pascal VOC, custom format exports.
- ✅ **Test:** Validate output files for all formats.

---

## 🔵 Phase 4: GUI & Interactive App

### PR20: Streamlit App Core
- Basic app to trigger pipeline via GUI.
- ✅ **Test:** End-to-end test with sample video → predictions.

### PR21: Configuration Management in GUI
- Load, display, edit, save `config.yaml`.
- ✅ **Test:** Simulate user interactions and config file integrity.

### PR22: Label Visualization
- Overlay bounding boxes/segmentations on frames in GUI.
- ✅ **Test:** Render outputs for known predictions.

### PR23: Model Switching via GUI
- Dropdown to select different models.
- ✅ **Test:** Confirm correct model loads, inference works post-switch.

---

## 🔵 Phase 5: Ensemble, Confidence, and Advanced Features

### PR24: Multi-Model Ensemble
- Run multiple models in parallel, aggregate outputs.
- ✅ **Test:** Parallel inference works, outputs combined.

### PR25: Agreement Analysis
- Compare outputs across models for agreement metrics.
- ✅ **Test:** Mock predictions to validate metric correctness.

### PR26: Confidence Scoring
- Include per-prediction confidence across models.
- ✅ **Test:** Scores computed correctly for known outputs.

### PR27: Fine-tuned Model Support
- Load custom user-provided fine-tuned models.
- ✅ **Test:** Model path from config, inference runs.

### PR28: Advanced Config for Ensembles
- Add weights, parameters per model in config.
- ✅ **Test:** Weighted ensemble calculations.

### PR29: Export Versioning
- Auto-increment export filenames (e.g. export_v3.json).
- ✅ **Test:** Ensure unique filenames per export run.

---

## 🔵 Phase 6: Deployment Finalization & Monitoring

### PR30: Performance Dashboard
- Streamlit dashboard showing per-model accuracy, agreement, performance visuals.
- ✅ **Test:** Load metrics from mock data, visualize correctly.

### PR31: Batch Processing Interface
- GUI for submitting batch jobs, track progress.
- ✅ **Test:** Simulated batch with status tracking.

### PR32: Sophisticated Ensemble Methods
- Add voting consensus, NMS, uncertainty quantification.
- ✅ **Test:** Unit tests for each ensemble method.

### PR33: Custom Model Integration in GUI
- UI + backend for uploading custom models into the pipeline.
- ✅ **Test:** Uploaded model path works, inference validated.

### PR34: Full Docker Build with GUI + Backend
- Docker image with complete app stack.
- ✅ **Test:** CI build of Docker image, functional tests inside container.

### PR35: Database Schema Implementation
- Add Projects, Models, Predictions, Ensembles, Frames schema.
- ✅ **Test:** CRUD operations, data integrity.

### PR36: Monitoring & Logging
- Centralized logging, error reporting, performance monitoring.
- ✅ **Test:** Mock failures produce logs, monitoring metrics captured.

---

## ✅ Bonus: Standard PR Checklist Template

- [ ] Feature implementation
- [ ] Corresponding unit tests
- [ ] CI passing (lint, mypy, tests)
- [ ] Documentation (docstrings, usage if applicable)
- [ ] Manual verification if UI/CLI
- [ ] Update changelog