#!/bin/bash
set -euo pipefail
echo "Setting up Bug Fix Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
