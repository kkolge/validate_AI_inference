# User Manual - YOLOv8 Inference Validation Tool

## Table of Contents

1. [Getting Started](#getting-started)
2. [Interface Overview](#interface-overview)
3. [Loading Your Dataset](#loading-your-dataset)
4. [Validating Images](#validating-images)
5. [Manual Entry](#manual-entry)
6. [Navigation](#navigation)
7. [Exporting Data](#exporting-data)
8. [Keyboard Shortcuts](#keyboard-shortcuts)
9. [Tips & Best Practices](#tips--best-practices)
10. [Troubleshooting](#troubleshooting)

---

## Getting Started

### Launch the Application

**Using the executable:**
```bash
./YOLOv8_Validator
```

**Using Python:**
```bash
python run.py
```

The application window will open with the main interface.

---

## Interface Overview

The interface is divided into several sections:

```
┌─────────────────────────────────────────────────┐
│ Configuration (Browse & Load)                   │
├─────────────────────────────────────────────────┤
│ Summary: Total | With Labels | Without Labels   │
│ Progress: X of Y processed                      │
├───────────────────────┬─────────────────────────┤
│                       │ Detected Objects        │
│   Image Preview       ├─────────────────────────┤
│   (Large Display)     │ Manual Entry            │
│                       │ (2-column layout)       │
└───────────────────────┴─────────────────────────┘
│ Navigation: Previous | Next | Save | Export     │
└─────────────────────────────────────────────────┘
```

### Sections Explained

1. **Configuration**: Select folders and load dataset
2. **Summary**: Dataset statistics and progress
3. **Image Preview**: View current image (expandable)
4. **Detected Objects**: Auto-detected counts from labels
5. **Manual Entry**: Add/correct counts manually
6. **Navigation**: Move between images and save data

---

## Loading Your Dataset

### Step 1: Select Results Folder

1. Click **Browse** next to "Results Folder"
2. Navigate to your YOLOv8 inference results folder
3. This folder should contain:
   - Image files (`.jpg`, `.png`)
   - A `labels/` subfolder with `.txt` label files

**Example folder structure:**
```
yolov8_batch_test_results/
├── image1.jpg
├── image2.jpg
├── ...
└── labels/
    ├── image1.txt
    ├── image2.txt
    └── ...
```

### Step 2: Select Class Configuration

1. Click **Browse** next to "Class Config (YAML)"
2. Select your `data.yaml` file
3. This file contains class names and dataset configuration

**Example data.yaml:**
```yaml
nc: 3
names: ['car', 'truck', 'bus']
```

### Step 3: Load Dataset

1. Click **Load Dataset**
2. Wait for validation to complete
3. You'll see:
   - Dataset summary (total images, with/without labels)
   - First image displayed
   - Navigation buttons enabled

**Success message** confirms dataset loaded successfully.

---

## Validating Images

### Understanding Detection Display

The **Detected Objects** panel shows auto-detected counts:

- **Green text**: Objects detected successfully
- **Blue text**: No objects detected (empty label file)
- **Orange text**: No label file found (requires manual entry)

**Example:**
```
Car: 3
Truck: 1
Bus: 0
```

### Image Information

At the bottom of the image preview:
- **Filename**: Current image name
- **File counter**: Position in dataset

---

## Manual Entry

### When to Use Manual Entry

- **Missing labels**: No label file exists
- **Incorrect detections**: Model missed or misidentified objects
- **Additional validation**: Verify model accuracy

### How to Add/Correct Counts

1. Locate the class in the **Manual Entry** section
2. Use the spinbox to set the count:
   - Click up/down arrows
   - Or type the number directly
3. Repeat for all classes that need correction
4. Click **Save Current** to store your entries

**Two-column layout** displays classes efficiently:
```
Class Name         Count    Class Name         Count
Car                [2]      Truck              [1]
Bus                [0]      Motorcycle         [0]
```

### Counts Explained

- **0**: No objects of this class
- **1-100**: Number of objects counted
- Values persist when you navigate away and return

---

## Navigation

### Moving Between Images

**Using buttons:**
- Click **← Previous** for the previous image
- Click **Next →** for the next image

**Using keyboard:**
- Press `←` (left arrow) for previous
- Press `→` (right arrow) for next

### Saving Progress

**Save current image:**
- Click **Save Current** button
- Or press `Ctrl+S`

**Auto-advance**: After saving, the tool automatically moves to the next image.

### Progress Tracking

Monitor your progress in the summary bar:
```
Progress: 45 of 455 processed
```

- **Processed**: Images you've reviewed and saved
- **Total**: All images in the dataset

---

## Exporting Data

### When to Export

Export when:
- You've validated all images
- You want to save intermediate progress
- You need data for analysis

### Export Process

1. Click **Export to CSV** button (or press `Ctrl+E`)
2. Choose save location and filename
3. Click **Save**

**Success message** confirms export completed.

### CSV Output Format

Each row represents one image:

| Column | Description |
|--------|-------------|
| `image_name` | Image filename |
| `has_label_file` | Yes/No |
| `detected_<class>` | Auto-detected count per class |
| `manual_<class>` | Manually entered count per class |
| `total_detected` | Sum of detected objects |
| `total_manual` | Sum of manual entries |
| `processed` | Processing status |

**Example CSV:**
```csv
image_name,has_label_file,detected_car,manual_car,total_detected,total_manual
img1.jpg,Yes,3,0,3,0
img2.jpg,No,0,2,0,2
```

### Using Exported Data

- **Excel**: Open CSV directly for analysis
- **Python**: Use pandas: `df = pd.read_csv('data.csv')`
- **R**: Use: `data <- read.csv('data.csv')`

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `←` | Previous image |
| `→` | Next image |
| `Ctrl+S` | Save current image data |
| `Ctrl+E` | Export to CSV |

**Tip**: Use keyboard shortcuts for faster workflow!

---

## Tips & Best Practices

### Efficiency Tips

1. **Use keyboard shortcuts** for faster navigation
2. **Save frequently** to avoid losing work
3. **Export periodically** as backup
4. **Review in batches** - validate 50-100 images, then export

### Quality Assurance

1. **Double-check manual entries** before saving
2. **Compare detected vs manual** to assess model accuracy
3. **Note patterns** - classes that are frequently missed
4. **Document issues** separately for model improvement

### Workflow Recommendations

**Initial review:**
1. Load dataset
2. Quickly scan first 10-20 images
3. Identify common detection issues

**Batch processing:**
1. Validate 50 images
2. Export progress
3. Take a break
4. Continue with next batch

**Final steps:**
1. Ensure all images are processed
2. Export final dataset
3. Analyze results in your preferred tool

---

## Troubleshooting

### Common Issues

**Problem**: Images appear too small
- **Solution**: Maximize the window or resize it larger

**Problem**: Can't see all manual entry fields
- **Solution**: Scroll down in the Manual Entry panel

**Problem**: Navigation buttons are disabled
- **Solution**: Load a dataset first (Browse → Select → Load)

**Problem**: Save button doesn't work
- **Solution**: Ensure dataset is loaded and you're on a valid image

**Problem**: Export fails
- **Solution**: Ensure at least one image is marked as "processed"

### Data Issues

**Problem**: "No images found"
- **Check**: Results folder contains `.jpg` or `.png` files
- **Check**: File permissions are correct

**Problem**: "No label file found" for all images
- **Check**: `labels/` subfolder exists
- **Check**: Label filenames match image filenames (except extension)

**Problem**: YAML file won't load
- **Check**: File contains `names` and `nc` fields
- **Check**: YAML syntax is valid

### Performance Issues

**Problem**: Application is slow
- **Solution**: Close other applications
- **Solution**: Process fewer images per session
- **Solution**: Use smaller image sizes if possible

---

## Getting Help

If you encounter issues:

1. Check this manual's Troubleshooting section
2. Review the README.md for setup instructions
3. Check the GitHub Issues page
4. Verify your data.yaml format matches examples

---

## Appendix: File Formats

### YOLO Label Format

Each line in a label file:
```
class_id x_center y_center width height
```

Example (`image1.txt`):
```
0 0.5 0.5 0.3 0.4
1 0.7 0.3 0.2 0.2
```

### data.yaml Format

```yaml
path: /path/to/dataset
train: train/images
val: val/images
test: test/images

nc: 12

names: ['class1', 'class2', ...]
```

---

**Version**: 1.0.0  
**Last Updated**: December 2025
