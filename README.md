# YOLOv8 Inference Validation Tool

<div align="center">

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20macos-lightgrey.svg)

**A professional GUI tool for validating and analyzing YOLOv8 object detection results**

[Features](#-features) • [Installation](#-installation) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [Contributing](#-contributing)

</div>

---

## 📋 Overview

The YOLOv8 Inference Validation Tool is a comprehensive desktop application designed to streamline the validation and analysis of YOLOv8 model inference results. Built with Python and tkinter, it provides an intuitive interface for reviewing predictions, correcting annotations, and exporting validation data.

**Perfect for:**
- 🎯 Quality assurance of model predictions
- 📊 Statistical analysis of detection results  
- ✏️ Manual annotation correction
- 🔍 Model performance evaluation
- 📈 Dataset validation workflows

---

## ✨ Features

### 🖼️ **Image Visualization**
- Large, auto-scaling image display optimized for detail review
- Support for JPG and PNG formats
- Responsive layout that adapts to your screen

### 📊 **Detection Analysis**
- View auto-detected object counts by class
- Color-coded status indicators (detected, empty, missing)
- Compact display supporting multiple classes
- Identify missing or problematic label files

### ✏️ **Manual Validation**
- Add or correct object counts for any class
- Two-column layout for efficient data entry
- Persistent storage - your edits are saved per image
- Spinbox controls for quick count adjustment

### 📈 **Progress Tracking**
- Real-time validation progress indicator
- Dataset summary statistics
- Visual tracking of processed vs. unprocessed images

### 💾 **Data Export**
- Export comprehensive validation data to CSV
- One row per image with detected and manual counts
- Includes metadata and processing status
- Ready for analysis in Excel, Python, R, or other tools

### ⌨️ **Productivity Features**
- Keyboard shortcuts for fast navigation
- Auto-advance after saving
- Batch processing support
- Scrollable panels for large class lists

---

## 🚀 Installation

### Option 1: Standalone Executable (Recommended)

**No Python installation required!**

1. Download the latest release from [Releases](https://github.com/yourusername/yolov8-validator/releases)
2. Extract and run:
   ```bash
   chmod +x YOLOv8_Validator
   ./YOLOv8_Validator
   ```

### Option 2: Run from Source

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yolov8-validator.git
   cd yolov8-validator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run:
   ```bash
   python run.py
   ```

### Option 3: Build Your Own

See [docs/BUILD.md](docs/BUILD.md) for instructions on creating executables.

**Detailed installation instructions:** [docs/INSTALLATION.md](docs/INSTALLATION.md)

---

## 🎯 Quick Start

1. **Launch the application**
   ```bash
   python run.py  # or ./YOLOv8_Validator
   ```

2. **Load your dataset**
   - Browse to your YOLOv8 results folder (with images and `labels/` subfolder)
   - Select your `data.yaml` configuration file
   - Click **Load Dataset**

3. **Validate images**
   - Review detected objects
   - Add/correct counts in Manual Entry section
   - Click **Save Current** (Ctrl+S)
   - Navigate with Previous/Next or arrow keys

4. **Export results**
   - Click **Export to CSV** (Ctrl+E)
   - Choose save location
   - Analyze in your preferred tool

**Full user manual:** [docs/USER_MANUAL.md](docs/USER_MANUAL.md)

---

## 📁 Project Structure

```
yolov8-validator/
├── src/
│   └── yolo_validator/
│       ├── __init__.py
│       ├── app.py              # Main application
│       ├── build.sh            # Build script
│       ├── yolo_validator.spec # PyInstaller config
│       └── modules/
│           ├── validator.py    # Validation logic
│           ├── yaml_parser.py  # YAML parser
│           └── data_exporter.py # CSV exporter
├── docs/
│   ├── USER_MANUAL.md          # Comprehensive user guide
│   ├── INSTALLATION.md         # Installation instructions
│   ├── BUILD.md                # Build documentation
│   └── examples/               # Configuration examples
├── tests/
│   └── test_modules.py         # Module unit tests
├── assets/                     # Screenshots and media
├── run.py                      # Entry point
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── LICENSE                     # MIT License
└── CONTRIBUTING.md             # Contribution guidelines
```

---

## 📖 Documentation

| Document | Description |
|----------|-------------|
| [USER_MANUAL.md](docs/USER_MANUAL.md) | Complete user guide |
| [INSTALLATION.md](docs/INSTALLATION.md) | Detailed installation instructions |
| [BUILD.md](docs/BUILD.md) | Building executables from source |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute |

---

## 💡 Use Cases

- **Model Evaluation**: Validate YOLOv8 predictions against ground truth
- **Quality Control**: Identify and correct detection errors
- **Dataset Preparation**: Validate annotations before training
- **Performance Analysis**: Export data for statistical analysis
- **Batch Processing**: Efficiently validate large image datasets

---

## 🛠️ Requirements

- **Python**: 3.7+ (if running from source)
- **OS**: Linux, Windows, macOS
- **RAM**: 2 GB minimum, 4 GB recommended
- **Display**: 1024x768 or higher

**Dependencies:**
- Pillow >= 10.0.0 (image processing)
- PyYAML >= 6.0 (configuration parsing)
- pytest >= 9.0 (testing, development only)

---

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `←` | Previous image |
| `→` | Next image |
| `Ctrl+S` | Save current |
| `Ctrl+E` | Export to CSV |

---

## 📊 CSV Export Format

```csv
image_name,has_label_file,detected_car,detected_truck,manual_car,manual_truck,total_detected,total_manual,processed
image1.jpg,Yes,3,1,0,0,4,0,Yes
image2.jpg,No,0,0,2,1,0,3,Yes
```

**Columns:**
- Image filename and label status
- Detected counts per class
- Manual counts per class
- Totals and processing status

---

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Ways to contribute:**
- 🐛 Report bugs
- 💡 Suggest features
- 📝 Improve documentation
- 🔧 Submit pull requests

---

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Ketan Kolge**
- Email: k_kolge@yahoo.com
- GitHub: [@kkolge](https://github.com/kkolge)

---

## 🙏 Acknowledgments

- Built with Python and tkinter for cross-platform compatibility
- Uses Pillow (PIL) for image processing
- Supports YOLOv8 label format and configuration
- Inspired by the need for efficient validation workflows

---

## 📧 Support

- **Documentation**: Check [docs/](docs/) folder
- **Issues**: GitHub Issues
- **Discussions**: GitHub Discussions
- **Contact**: k_kolge@yahoo.com

---

## 🗺️ Roadmap

- [x] Automated testing suite
- [ ] Bounding box visualization on images
- [ ] Support for additional label formats
- [ ] Batch export with summary statistics
- [ ] Dark mode UI theme
- [ ] Windows and macOS executables

---

<div align="center">

**Made with ❤️ for the computer vision community**

⭐ Star this repo if you find it helpful!

</div>
