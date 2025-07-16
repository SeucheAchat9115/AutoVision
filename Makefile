# AutoVision Development Makefile
.PHONY: help install test test-unit test-integration test-slow lint format type-check security clean build
.DEFAULT_GOAL := help

help: ## Show this help message
	@echo "AutoVision Development Commands:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install project dependencies with uv
	uv sync --all-extras --dev

install-pre-commit: ## Install pre-commit hooks
	uv run pre-commit install

test: ## Run all tests
	uv run pytest tests/ --cov=autovision --cov-report=term-missing --cov-report=html

test-unit: ## Run unit tests only
	uv run pytest tests/ -m "unit" --cov=autovision --cov-report=term-missing

test-integration: ## Run integration tests only
	uv run pytest tests/ -m "integration" --cov=autovision --cov-report=term-missing

test-slow: ## Run slow tests
	uv run pytest tests/ -m "slow" --cov=autovision --cov-report=term-missing

test-watch: ## Run tests in watch mode
	uv run pytest-watch tests/ -m "unit"

lint: ## Run linting with ruff
	uv run ruff check .

lint-fix: ## Run linting with automatic fixes
	uv run ruff check . --fix

format: ## Format code with ruff
	uv run ruff format .

format-check: ## Check code formatting
	uv run ruff format . --check

type-check: ## Run type checking with mypy
	uv run mypy src/autovision tests

security: ## Run security checks
	uv run bandit -r src/autovision
	uv run safety check

quality: lint format-check type-check security ## Run all quality checks

clean: ## Clean build artifacts and cache
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf coverage.xml
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

build: ## Build the package
	uv build

build-dev: ## Build development version
	uv build --wheel

install-local: build ## Install package locally
	uv pip install dist/*.whl --force-reinstall

test-install: ## Test installation in clean environment
	uv run --isolated pip install dist/*.whl
	uv run --isolated python -c "import autovision; print(autovision.__version__)"

dev-setup: install install-pre-commit ## Complete development environment setup
	@echo "Development environment ready!"
	@echo "Run 'make test' to validate setup"

ci-test: ## Run CI-like test suite locally
	uv run ruff check .
	uv run ruff format . --check
	uv run mypy src/autovision tests
	uv run pytest tests/ -m "unit" --cov=autovision --cov-fail-under=80

release-check: clean build test-install ## Check if package is ready for release
	@echo "Package ready for release!"
