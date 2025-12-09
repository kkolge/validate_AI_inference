# Installation Guide

## Quick Installation Options

### Option 1: Standalone Executable (Recommended for Users)

**No Python installation required!**

1. Download the latest release from the [Releases page](https://github.com/yourusername/yolov8-validator/releases)
2. Extract the archive
3. Make executable (Linux/macOS):
   ```bash
   chmod +x YOLOv8_Validator
   ```
4. Run:
   ```bash
   ./YOLOv8_Validator
   ```

**Supported Platforms:**
- Linux (64-bit)
- Windows (coming soon)
- macOS (coming soon)

---

## Option 2: Install from Source (For Developers)

### Prerequisites

- **Python 3.7 or higher**
- **pip** (Python package manager)
- **tkinter** (usually included with Python)

Check your Python version:
```bash
python --version
```

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/yolov8-validator.git
   cd yolov8-validator
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # or
   venv\Scripts\activate  # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run tests (optional):**
   ```bash
   pytest tests/ -v
   ```

5. **Run the application:**
   ```bash
   python run.py
   ```

---

## Option 3: Install as Python Package

Coming soon - installable via pip:
```bash
pip install yolov8-validator
```

---

## Verifying Installation

### Test the Application

1. Launch the application
2. You should see the main window with:
   - Configuration section at top
   - Image preview area
   - Detection and manual entry panels

### Test with Sample Data

If you have YOLOv8 inference results:

1. Click **Browse** and select your results folder
2. Click **Browse** and select your data.yaml
3. Click **Load Dataset**
4. Navigate through images with arrow keys

---

## System Requirements

### Minimum Requirements

- **OS**: Linux (Ubuntu 18.04+), Windows 10+, macOS 10.14+
- **RAM**: 2 GB
- **Disk Space**: 100 MB (plus space for your images)
- **Display**: 1024x768 or higher

### Recommended

- **OS**: Linux (Ubuntu 20.04+), Windows 11, macOS 11+
- **RAM**: 4 GB or more
- **Disk Space**: 500 MB
- **Display**: 1920x1080 or higher

---

## Dependency Details

### Required Python Packages

```
Pillow >= 10.0.0      # Image processing
PyYAML >= 6.0         # YAML configuration parsing
```

### Optional (Development Only)

```
pyinstaller >= 6.0    # For building executables
pytest >= 7.0         # For running tests
```

---

## Platform-Specific Notes

### Linux

**Ubuntu/Debian:**
```bash
# Install tkinter if not present
sudo apt-get update
sudo apt-get install python3-tk

# Install pillow dependencies
sudo apt-get install libjpeg-dev zlib1g-dev
```

**Fedora/RHEL:**
```bash
sudo dnf install python3-tkinter
```

### Windows

- Python from [python.org](https://python.org) includes tkinter
- No additional steps needed

### macOS

- Python from [python.org](https://python.org) includes tkinter
- Homebrew Python includes tkinter
- No additional steps needed

---

## Building from Source

For creating your own executable, see [BUILD.md](BUILD.md)

Quick build:
```bash
cd src/yolo_validator
./build.sh
```

Executable will be in `dist/YOLOv8_Validator`

---

## Troubleshooting Installation

### Common Issues

**Problem**: `ModuleNotFoundError: No module named 'tkinter'`
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# macOS
brew install python-tk
```

**Problem**: `pip: command not found`
```bash
# Install pip
python -m ensurepip --upgrade
```

**Problem**: Permission denied when running executable
```bash
chmod +x YOLOv8_Validator
```

**Problem**: Import errors after installation
```bash
# Reinstall dependencies
pip install --force-reinstall -r requirements.txt
```

---

## Updating

### Update from Source

```bash
cd yolov8-validator
git pull origin main
pip install --upgrade -r requirements.txt
```

### Update Executable

Download the latest release and replace the old executable.

---

## Uninstalling

### Remove Source Installation

```bash
# Deactivate virtual environment if active
deactivate

# Remove directory
cd ..
rm -rf yolov8-validator
```

### Remove Executable

Simply delete the `YOLOv8_Validator` file.

---

## Getting Help

- **Documentation**: See [README.md](../README.md)
- **User Manual**: See [USER_MANUAL.md](USER_MANUAL.md)
- **Issues**: Report on [GitHub Issues](https://github.com/yourusername/yolov8-validator/issues)

---

**Last Updated**: December 2025
