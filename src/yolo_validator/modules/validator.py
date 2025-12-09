"""
Module for validating YOLOv8 inference results.
Handles image and label file validation.
"""

from pathlib import Path
from typing import Dict, List, Optional
import os


class InferenceValidator:
    """Validator for YOLOv8 inference results."""
    
    SUPPORTED_IMAGE_FORMATS = {'.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG'}
    
    def __init__(self, results_folder: Path, class_names: Dict[int, str]):
        """
        Initialize the validator.
        
        Args:
            results_folder: Path to the folder containing inference results
            class_names: Dictionary mapping class IDs to class names
        """
        self.results_folder = Path(results_folder)
        self.labels_folder = self.results_folder / 'labels'
        self.class_names = class_names
        
        if not self.results_folder.exists():
            raise ValueError(f"Results folder does not exist: {self.results_folder}")
    
    def get_image_files(self) -> List[Path]:
        """
        Get all image files from the results folder.
        
        Returns:
            List of image file paths, sorted by name
        """
        image_files = []
        
        for file_path in self.results_folder.iterdir():
            if file_path.is_file() and file_path.suffix in self.SUPPORTED_IMAGE_FORMATS:
                image_files.append(file_path)
        
        return sorted(image_files)
    
    def get_label_file(self, image_path: Path) -> Optional[Path]:
        """
        Get the corresponding label file for an image.
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Path to label file if it exists, None otherwise
        """
        # Get image stem (filename without extension)
        image_stem = image_path.stem
        
        # Construct label file path
        label_path = self.labels_folder / f"{image_stem}.txt"
        
        return label_path if label_path.exists() else None
    
    def validate_labels(self) -> Dict:
        """
        Validate that label files exist for images.
        
        Returns:
            Dictionary with validation summary
        """
        image_files = self.get_image_files()
        
        images_with_labels = 0
        images_without_labels = 0
        
        for image_path in image_files:
            if self.get_label_file(image_path) is not None:
                images_with_labels += 1
            else:
                images_without_labels += 1
        
        return {
            'total_images': len(image_files),
            'images_with_labels': images_with_labels,
            'images_without_labels': images_without_labels
        }
    
    def get_detections(self, image_path: Path) -> Optional[List[int]]:
        """
        Get detection class IDs from the label file.
        
        Args:
            image_path: Path to the image file
            
        Returns:
            List of class IDs if label file exists, None if no label file,
            empty list if label file exists but has no detections
        """
        label_path = self.get_label_file(image_path)
        
        if label_path is None:
            return None
        
        class_ids = []
        
        try:
            with open(label_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    
                    # Parse YOLO format: class_id x_center y_center width height
                    parts = line.split()
                    if len(parts) >= 5:
                        class_id = int(parts[0])
                        class_ids.append(class_id)
        
        except Exception as e:
            print(f"Error reading label file {label_path}: {e}")
            return []
        
        return class_ids
    
    def parse_label_file(self, label_path: Path) -> List[Dict]:
        """
        Parse a YOLO label file and return detailed information.
        
        Args:
            label_path: Path to the label file
            
        Returns:
            List of dictionaries with detection information
        """
        detections = []
        
        try:
            with open(label_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    
                    parts = line.split()
                    if len(parts) >= 5:
                        class_id = int(parts[0])
                        x_center = float(parts[1])
                        y_center = float(parts[2])
                        width = float(parts[3])
                        height = float(parts[4])
                        
                        detections.append({
                            'class_id': class_id,
                            'class_name': self.class_names.get(class_id, f"Unknown ({class_id})"),
                            'x_center': x_center,
                            'y_center': y_center,
                            'width': width,
                            'height': height
                        })
        
        except Exception as e:
            print(f"Error parsing label file {label_path}: {e}")
        
        return detections
