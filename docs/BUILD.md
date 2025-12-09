# Building Executable

## Quick Build

To create a standalone executable:

```bash
./build.sh
```

The executable will be created at `dist/YOLOv8_Validator`

## Manual Build

If you prefer to build manually:

```bash
# Clean previous builds
rm -rf build/ dist/

# Build using PyInstaller
pyinstaller --clean yolo_validator.spec
```

## Running the Executable

```bash
./dist/YOLOv8_Validator
```

Or double-click the file in your file manager.

## Build Specifications

- **Build tool**: PyInstaller
- **Executable size**: ~20 MB
- **Platform**: Linux (64-bit)
- **GUI mode**: No console window
- **Dependencies**: All bundled (Pillow, PyYAML, tkinter)

## Distribution

To distribute the application:

1. Copy the `dist/YOLOv8_Validator` file to the target system
2. Make it executable: `chmod +x YOLOv8_Validator`
3. Run: `./YOLOv8_Validator`

No Python installation required on the target system!

## Build Files

- `yolo_validator.spec` - PyInstaller configuration
- `build.sh` - Automated build script
- `build/` - Temporary build files (auto-cleaned)
- `dist/` - Final executable output

## Troubleshooting

**Issue**: Build fails with missing modules
- Solution: Ensure all dependencies are installed: `pip install -r requirements.txt`

**Issue**: Executable doesn't run
- Solution: Check file permissions: `chmod +x dist/YOLOv8_Validator`
- Check for missing system libraries: `ldd dist/YOLOv8_Validator`

**Issue**: Large file size
- The executable includes Python interpreter and all dependencies
- This is normal for PyInstaller bundles
- Consider using `--onedir` mode if size is critical (requires distributing folder)

## Cross-Platform Builds

PyInstaller creates executables for the platform it runs on.

- **Linux**: Build on Linux → Linux executable
- **Windows**: Build on Windows → .exe file
- **macOS**: Build on macOS → macOS app

For Windows builds, update `yolo_validator.spec`:
```python
exe = EXE(
    ...
    name='YOLOv8_Validator.exe',  # Add .exe extension
    icon='icon.ico',  # Optional: Add application icon
    ...
)
```
