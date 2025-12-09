#!/bin/bash
# Build script for YOLOv8 Inference Validation Tool

echo "Building YOLOv8 Validator executable..."
echo "========================================"

# Get the project root directory
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf build/ dist/

# Build the executable
echo "Running PyInstaller..."
cd src/yolo_validator
pyinstaller --clean yolo_validator.spec

# Move executable to project root dist folder
mkdir -p "$PROJECT_ROOT/dist"
if [ -f "dist/YOLOv8_Validator" ]; then
    mv dist/YOLOv8_Validator "$PROJECT_ROOT/dist/"
    rm -rf dist/ build/
fi

cd "$PROJECT_ROOT"

# Check if build was successful
if [ -f "dist/YOLOv8_Validator" ]; then
    echo ""
    echo "✓ Build successful!"
    echo "Executable location: dist/YOLOv8_Validator"
    echo ""
    echo "File size:"
    ls -lh dist/YOLOv8_Validator
    echo ""
    echo "To run the executable:"
    echo "  ./dist/YOLOv8_Validator"
else
    echo ""
    echo "✗ Build failed!"
    exit 1
fi
