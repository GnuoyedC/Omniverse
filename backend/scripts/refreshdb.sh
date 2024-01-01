#!/bin/bash

SCRIPT_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$( cd "$SCRIPT_ROOT/.." && pwd)"

source "$PROJECT_ROOT/../venv/bin/activate"
echo "Activated the virtual environment."

python "$PROJECT_ROOT/utils/script_helper.py"
