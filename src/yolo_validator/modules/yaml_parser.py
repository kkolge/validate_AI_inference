"""
Module for parsing YOLOv8 data.yaml configuration files.
"""

import yaml
from pathlib import Path
from typing import Dict, List, Optional


class YAMLParser:
    """Parser for YOLO data.yaml configuration files."""
    
    def __init__(self, yaml_path: Path):
        """
        Initialize the YAML parser.
        
        Args:
            yaml_path: Path to the data.yaml file
        """
        self.yaml_path = Path(yaml_path)
        
        if not self.yaml_path.exists():
            raise FileNotFoundError(f"YAML file not found: {self.yaml_path}")
        
        self.data = self._load_yaml()
        self._validate_yaml()
    
    def _load_yaml(self) -> Dict:
        """
        Load the YAML file.
        
        Returns:
            Dictionary containing YAML data
        """
        try:
            with open(self.yaml_path, 'r') as f:
                data = yaml.safe_load(f)
            return data
        except Exception as e:
            raise ValueError(f"Failed to parse YAML file: {e}")
    
    def _validate_yaml(self):
        """Validate that required fields exist in the YAML."""
        if 'names' not in self.data:
            raise ValueError("YAML file must contain 'names' field")
        
        if 'nc' not in self.data:
            raise ValueError("YAML file must contain 'nc' (number of classes) field")
    
    def get_class_names(self) -> Dict[int, str]:
        """
        Get class names from the YAML file.
        
        Returns:
            Dictionary mapping class IDs to class names
        """
        names = self.data['names']
        
        # Handle both list and dict formats
        if isinstance(names, list):
            # List format: ['class1', 'class2', ...]
            return {i: name for i, name in enumerate(names)}
        elif isinstance(names, dict):
            # Dict format: {0: 'class1', 1: 'class2', ...}
            return {int(k): str(v) for k, v in names.items()}
        else:
            raise ValueError(f"Unsupported 'names' format in YAML: {type(names)}")
    
    def get_num_classes(self) -> int:
        """
        Get the number of classes.
        
        Returns:
            Number of classes
        """
        return int(self.data['nc'])
    
    def get_dataset_path(self) -> Optional[str]:
        """
        Get the dataset path if specified.
        
        Returns:
            Dataset path or None
        """
        return self.data.get('path')
    
    def get_split_paths(self) -> Dict[str, str]:
        """
        Get train/val/test split paths.
        
        Returns:
            Dictionary with split paths
        """
        splits = {}
        
        for split_name in ['train', 'val', 'test']:
            if split_name in self.data:
                splits[split_name] = self.data[split_name]
        
        return splits
    
    def get_all_data(self) -> Dict:
        """
        Get all data from the YAML file.
        
        Returns:
            Complete YAML data dictionary
        """
        return self.data.copy()
