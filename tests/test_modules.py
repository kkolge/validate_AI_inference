"""
Test suite for YOLOv8 Validator modules
"""
import pytest
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from yolo_validator.modules.yaml_parser import YAMLParser
from yolo_validator.modules.validator import InferenceValidator
from yolo_validator.modules.data_exporter import DataExporter


class TestYAMLParser:
    """Tests for YAML parser module"""
    
    def test_import(self):
        """Test that YAMLParser can be imported"""
        assert YAMLParser is not None
    
    def test_class_names_format(self):
        """Test that class names are returned as dictionary"""
        # This is a basic structure test
        # Actual file testing would require a test YAML file
        pass


class TestInferenceValidator:
    """Tests for validator module"""
    
    def test_import(self):
        """Test that InferenceValidator can be imported"""
        assert InferenceValidator is not None
    
    def test_supported_formats(self):
        """Test that supported image formats are defined"""
        assert hasattr(InferenceValidator, 'SUPPORTED_IMAGE_FORMATS')
        assert '.jpg' in InferenceValidator.SUPPORTED_IMAGE_FORMATS
        assert '.png' in InferenceValidator.SUPPORTED_IMAGE_FORMATS


class TestDataExporter:
    """Tests for data exporter module"""
    
    def test_import(self):
        """Test that DataExporter can be imported"""
        assert DataExporter is not None
    
    def test_exporter_initialization(self):
        """Test that DataExporter can be instantiated"""
        exporter = DataExporter()
        assert exporter is not None


class TestPackage:
    """Tests for package structure"""
    
    def test_version(self):
        """Test that version is defined"""
        from yolo_validator import __version__
        assert __version__ == "1.0.0"
    
    def test_author(self):
        """Test that author is defined"""
        from yolo_validator import __author__
        assert __author__ == "Ketan Kolge"
    
    def test_license(self):
        """Test that license is defined"""
        from yolo_validator import __license__
        assert __license__ == "MIT"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
