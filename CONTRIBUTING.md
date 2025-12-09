# Contributing to YOLOv8 Inference Validator

Thank you for considering contributing to this project! This document provides guidelines for contributing.

## How to Contribute

### Reporting Bugs

If you find a bug:

1. Check [existing issues](https://github.com/kkolge/yolov8-validator/issues) to avoid duplicates
2. Create a new issue with:
   - Clear, descriptive title
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots if applicable
   - System info (OS, Python version)

### Suggesting Features

Feature requests are welcome! Please:

1. Check existing issues/discussions
2. Describe the feature clearly
3. Explain the use case
4. Provide examples if possible

### Code Contributions

#### Setup Development Environment

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/kkolge/yolov8-validator.git
   cd yolov8-validator
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

#### Making Changes

1. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes:
   - Follow existing code style
   - Add comments for complex logic
   - Update documentation if needed

3. Test your changes:
   ```bash
   python run.py  # Test the application
   pytest tests/ -v  # Run tests
   ```

4. Commit your changes:
   ```bash
   git add .
   git commit -m "Add feature: description"
   ```

5. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

6. Create a Pull Request

#### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add docstrings to functions/classes
- Keep functions focused and small
- Comment complex logic

**Example:**
```python
def validate_labels(self) -> Dict:
    """
    Validate that label files exist for images.
    
    Returns:
        Dictionary with validation summary
    """
    # Implementation...
```

#### Project Structure

```
src/yolo_validator/
├── __init__.py           # Package initialization
├── app.py                # Main application
└── modules/
    ├── validator.py      # Validation logic
    ├── yaml_parser.py    # YAML parsing
    └── data_exporter.py  # Export functionality
```

### Documentation

When adding features:

1. Update relevant `.md` files
2. Add docstrings to new functions
3. Update USER_MANUAL.md if UI changes
4. Update README.md if installation changes

### Testing

We use pytest for automated testing. Before submitting PRs:

1. **Run existing tests:**
   ```bash
   pytest tests/ -v
   ```

2. **Add tests for new features:**
   - Create test files in `tests/` directory
   - Follow existing test patterns
   - Test both success and failure cases

**Test checklist:**
- [ ] All pytest tests pass
- [ ] Application launches without errors
- [ ] Dataset loads correctly
- [ ] Image navigation works
- [ ] Manual entry saves properly
- [ ] CSV export is valid
- [ ] Keyboard shortcuts work

## Pull Request Process

1. Ensure your PR:
   - Has a clear description
   - References related issues
   - Includes updated documentation
   - Has been tested

2. Wait for review
3. Address reviewer comments
4. Once approved, it will be merged

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Accept constructive criticism gracefully
- Focus on what's best for the project
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discriminatory language
- Trolling or insulting comments
- Publishing others' private information
- Other unprofessional conduct

## Questions?

Feel free to:
- Open a discussion on GitHub
- Comment on existing issues
- Reach out to maintainers

---

Thank you for contributing! 🎉
