#!/bin/bash
echo "Creating virtual environment and installing dependencies"
python -m venv venv
source venv/bin/activate
echo "Venv created ..."
echo "Installing project using uv"
uv sync
pre-commit install
echo "Project installed"
