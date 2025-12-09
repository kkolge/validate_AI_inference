#!/bin/bash
# Quick setup script for YOLOv8 Inference Validation Tool

echo "=================================="
echo "YOLOv8 Validator - Quick Setup"
echo "=================================="
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python --version 2>&1 | awk '{print $2}')
echo "Found Python $python_version"

if ! python -c 'import sys; sys.exit(0 if sys.version_info >= (3, 7) else 1)'; then
    echo "❌ Error: Python 3.7+ required"
    exit 1
fi

echo "✓ Python version OK"
echo ""

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""
echo "=================================="
echo "✓ Setup complete!"
echo "=================================="
echo ""
echo "To run the application:"
echo "  python run.py"
echo ""
echo "To build executable:"
echo "  cd src/yolo_validator"
echo "  ./build.sh"
echo ""
echo "For more information, see:"
echo "  - README.md"
echo "  - docs/USER_MANUAL.md"
echo "  - docs/INSTALLATION.md"
echo ""
