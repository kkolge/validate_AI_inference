# GitHub Release Checklist

Use this checklist when preparing for a GitHub release.

## Pre-Release

### Code
- [ ] All features working correctly
- [ ] No critical bugs
- [ ] Code is well-documented
- [ ] Import paths are correct
- [ ] Test with `python run.py`

### Documentation
- [ ] README.md is up to date
- [ ] USER_MANUAL.md reflects current UI
- [ ] INSTALLATION.md has correct steps
- [ ] All documentation links work
- [ ] Version numbers are consistent

### Build
- [ ] Executable builds successfully
- [ ] Test executable on clean system
- [ ] File size is reasonable
- [ ] All dependencies are bundled

## Repository Setup

### GitHub Repository
- [ ] Repository created on GitHub
- [ ] Repository name matches documentation
- [ ] Description added
- [ ] Topics/tags added (python, yolov8, gui, tkinter, computer-vision)
- [ ] License set to MIT

### Files
- [ ] .gitignore is comprehensive
- [ ] README.md has correct repository URLs
- [ ] CONTRIBUTING.md has correct links
- [ ] No sensitive data in repository

## First Commit

```bash
git init
git add .
git commit -m "Initial commit: YOLOv8 Inference Validation Tool v1.0.0"
git branch -M main
git remote add origin https://github.com/USERNAME/REPO.git
git push -u origin main
```

## Creating a Release

### Version Number
- [ ] Update version in `src/yolo_validator/__init__.py`
- [ ] Tag format: `v1.0.0`

### Build Executable
```bash
cd src/yolo_validator
./build.sh
```

### GitHub Release Steps
1. Go to repository → Releases → Create new release
2. Tag: `v1.0.0`
3. Title: `YOLOv8 Inference Validator v1.0.0`
4. Description:
   ```markdown
   ## YOLOv8 Inference Validation Tool v1.0.0
   
   First stable release!
   
   ### Features
   - GUI for validating YOLOv8 inference results
   - Manual annotation correction
   - CSV export for analysis
   - Keyboard shortcuts
   - Progress tracking
   
   ### Downloads
   - **Linux (64-bit)**: Download `YOLOv8_Validator` executable
   - **Source code**: Download zip/tar.gz
   
   ### Requirements
   - Python 3.7+ (source only)
   - No dependencies for executable
   
   ### Documentation
   - [User Manual](docs/USER_MANUAL.md)
   - [Installation Guide](docs/INSTALLATION.md)
   ```
5. Upload `dist/YOLOv8_Validator` as release asset
6. Mark as latest release
7. Publish

## Post-Release

### Announcements
- [ ] Update README.md with release link
- [ ] Share on relevant communities
- [ ] Update documentation if needed

### Monitoring
- [ ] Watch for issues
- [ ] Respond to questions
- [ ] Plan next features based on feedback

## Assets for Release

Recommended files to include:
- `YOLOv8_Validator` - Linux executable
- `YOLOv8_Validator.exe` - Windows executable (if available)
- Source code (automatic)
- `sample_data.zip` - Example dataset (optional)

## Screenshot Preparation

Before release, add screenshots to `assets/`:
- Main interface
- Dataset loaded
- Image with detections
- Manual entry in action
- CSV export

Update README.md to show screenshots.

## Update URLs

Replace placeholders in:
- [ ] README.md
- [ ] docs/INSTALLATION.md
- [ ] docs/USER_MANUAL.md
- [ ] CONTRIBUTING.md

Replace `yourusername` with actual GitHub username.

## Testing

Test on:
- [ ] Ubuntu 20.04+
- [ ] Ubuntu 18.04
- [ ] Fedora (if possible)
- [ ] Windows (if executable available)
- [ ] macOS (if executable available)

## Common Issues to Check

- [ ] Executable runs without Python installed
- [ ] All documentation links work
- [ ] License file is present
- [ ] Requirements.txt is up to date
- [ ] .gitignore excludes test data
- [ ] No hardcoded paths in code

## Version Numbering

Follow semantic versioning (MAJOR.MINOR.PATCH):
- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes

Current version: **1.0.0**
