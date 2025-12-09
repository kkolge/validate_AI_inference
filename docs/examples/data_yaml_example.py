#!/usr/bin/env python3
"""
YOLOv8 Inference Validation Tool - Example Configuration

This file shows the expected format for data.yaml configuration files
used with the YOLOv8 Inference Validation Tool.
"""

# Example 1: List format (most common)
example_list_format = """
# data.yaml

# Dataset root path
path: /path/to/your/dataset

# Relative paths to image folders
train: train/images
val: val/images
test: test/images

# Number of classes
nc: 12

# Class names (0-indexed list)
names: [
  '10-15: Truck',
  '16: Earth Moving Machinery',
  '17: Heavy Construction Machinery',
  '18: Tractor',
  '19: Tractor with Trailer',
  '1: Two Wheeler',
  '2/3: Three Wheeler',
  '20: Mini Light Commercial Vehicle',
  '4: Car / Jeep / Van',
  '5/6: Light Commercial Vehicle',
  '7/8: Bus',
  '9: Mini-Bus'
]
"""

# Example 2: Dictionary format (alternative)
example_dict_format = """
# data.yaml

path: /path/to/your/dataset
train: train/images
val: val/images
test: test/images

nc: 3

# Class names (dictionary format)
names:
  0: 'car'
  1: 'truck'
  2: 'bus'
"""

if __name__ == "__main__":
    print("YOLOv8 data.yaml Configuration Examples")
    print("=" * 50)
    print("\nExample 1 - List Format:")
    print(example_list_format)
    print("\nExample 2 - Dictionary Format:")
    print(example_dict_format)
    print("\nNote: Both formats are supported by the validation tool.")
