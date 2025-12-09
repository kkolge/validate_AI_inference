"""
Module for exporting validation data to various formats.
"""

import csv
from pathlib import Path
from typing import Dict, List
from datetime import datetime


class DataExporter:
    """Exporter for validation data."""
    
    def export_to_csv(self, validation_data: List[Dict], class_names: Dict[int, str], 
                      output_path: str):
        """
        Export validation data to CSV format.
        
        Args:
            validation_data: List of validation data dictionaries
            class_names: Dictionary mapping class IDs to class names
            output_path: Path to save the CSV file
        """
        if not validation_data:
            raise ValueError("No validation data to export")
        
        # Get all unique class names (sorted)
        all_class_names = sorted(set(class_names.values()))
        
        # Prepare CSV headers
        headers = ['image_name', 'has_label_file']
        
        # Add detected count columns
        for class_name in all_class_names:
            headers.append(f'detected_{class_name}')
        
        # Add manual count columns
        for class_name in all_class_names:
            headers.append(f'manual_{class_name}')
        
        # Add summary columns
        headers.extend(['total_detected', 'total_manual', 'processed'])
        
        # Write CSV
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            
            for item in validation_data:
                if not item.get('processed', False):
                    # Skip unprocessed items
                    continue
                
                row = {
                    'image_name': item.get('image_name', ''),
                    'has_label_file': 'Yes' if item.get('has_label_file', False) else 'No'
                }
                
                # Add detected counts
                detected_counts = item.get('detected_counts', {})
                total_detected = 0
                for class_name in all_class_names:
                    count = detected_counts.get(class_name, 0)
                    row[f'detected_{class_name}'] = count
                    total_detected += count
                
                # Add manual counts
                manual_counts = item.get('manual_counts', {})
                total_manual = 0
                for class_name in all_class_names:
                    count = manual_counts.get(class_name, 0)
                    row[f'manual_{class_name}'] = count
                    total_manual += count
                
                # Add summary
                row['total_detected'] = total_detected
                row['total_manual'] = total_manual
                row['processed'] = 'Yes'
                
                writer.writerow(row)
        
        print(f"Exported {sum(1 for item in validation_data if item.get('processed', False))} "
              f"records to {output_path}")
    
    def export_summary_stats(self, validation_data: List[Dict], class_names: Dict[int, str],
                            output_path: str):
        """
        Export summary statistics to CSV.
        
        Args:
            validation_data: List of validation data dictionaries
            class_names: Dictionary mapping class IDs to class names
            output_path: Path to save the summary CSV file
        """
        processed_data = [item for item in validation_data if item.get('processed', False)]
        
        if not processed_data:
            raise ValueError("No processed data to generate summary")
        
        # Calculate statistics per class
        all_class_names = sorted(set(class_names.values()))
        
        stats = []
        
        for class_name in all_class_names:
            total_detected = sum(
                item.get('detected_counts', {}).get(class_name, 0) 
                for item in processed_data
            )
            total_manual = sum(
                item.get('manual_counts', {}).get(class_name, 0) 
                for item in processed_data
            )
            
            images_with_detected = sum(
                1 for item in processed_data 
                if item.get('detected_counts', {}).get(class_name, 0) > 0
            )
            images_with_manual = sum(
                1 for item in processed_data 
                if item.get('manual_counts', {}).get(class_name, 0) > 0
            )
            
            stats.append({
                'class_name': class_name,
                'total_detected': total_detected,
                'total_manual': total_manual,
                'images_with_detected': images_with_detected,
                'images_with_manual': images_with_manual,
                'total_count': total_detected + total_manual
            })
        
        # Write summary CSV
        headers = ['class_name', 'total_detected', 'total_manual', 'total_count',
                  'images_with_detected', 'images_with_manual']
        
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(stats)
        
        print(f"Exported summary statistics to {output_path}")
    
    def get_export_metadata(self) -> Dict:
        """
        Get metadata for the export.
        
        Returns:
            Dictionary with export metadata
        """
        return {
            'export_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'exporter_version': '1.0.0'
        }
