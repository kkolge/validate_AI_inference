#!/usr/bin/env python3
"""
Main entry point for YOLOv8 Inference Validator
"""

import sys
from pathlib import Path

# Add src to path for imports
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from yolo_validator.app import main

if __name__ == "__main__":
    main()
