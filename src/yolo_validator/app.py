#!/usr/bin/env python3
"""
YOLOv8 Inference Validation Tool
A tkinter-based GUI application for validating YOLOv8 inference results.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from collections import Counter

from .modules.yaml_parser import YAMLParser
from .modules.validator import InferenceValidator
from .modules.data_exporter import DataExporter


class YOLOValidatorApp:
    """Main application class for YOLO inference validation."""
    
    def __init__(self, root: tk.Tk):
        """Initialize the application."""
        self.root = root
        self.root.title("YOLOv8 Inference Validator")
        
        # Data attributes
        self.results_folder: Optional[Path] = None
        self.yaml_file: Optional[Path] = None
        self.class_names: Dict[int, str] = {}
        self.images: List[Path] = []
        self.current_index: int = 0
        self.validation_data: List[Dict] = []
        
        # Validator and exporter
        self.validator: Optional[InferenceValidator] = None
        self.exporter = DataExporter()
        
        # UI components
        self.current_image_label: Optional[tk.Label] = None
        self.manual_entry_widgets: Dict[str, ttk.Spinbox] = {}
        
        self._setup_ui()
        self._bind_shortcuts()
    
    def _setup_ui(self):
        """Set up the user interface."""
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights for responsiveness
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=3)  # Left column (image) gets more space
        main_frame.columnconfigure(1, weight=1)  # Right column (controls)
        main_frame.rowconfigure(2, weight=1)     # Main content row expands
        
        # Top section - File selection
        self._create_file_selection_section(main_frame, row=0)
        
        # Summary section
        self._create_summary_section(main_frame, row=1)
        
        # Main content area - split into left (image) and right (controls)
        self._create_main_content_section(main_frame, row=2)
        
        # Navigation and export section
        self._create_navigation_section(main_frame, row=3)
    
    def _create_file_selection_section(self, parent: ttk.Frame, row: int):
        """Create the file selection section."""
        section_frame = ttk.LabelFrame(parent, text="Configuration", padding="5")
        section_frame.grid(row=row, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        section_frame.columnconfigure(1, weight=1)
        
        # Results folder selection
        ttk.Label(section_frame, text="Results Folder:").grid(row=0, column=0, sticky=tk.W, padx=5)
        self.folder_entry = ttk.Entry(section_frame, width=50)
        self.folder_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)
        ttk.Button(section_frame, text="Browse", command=self._browse_folder).grid(row=0, column=2, padx=5)
        
        # YAML file selection
        ttk.Label(section_frame, text="Class Config (YAML):").grid(row=1, column=0, sticky=tk.W, padx=5)
        self.yaml_entry = ttk.Entry(section_frame, width=50)
        self.yaml_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=5)
        ttk.Button(section_frame, text="Browse", command=self._browse_yaml).grid(row=1, column=2, padx=5)
        
        # Load button
        ttk.Button(section_frame, text="Load Dataset", command=self._load_dataset, 
                  style="Accent.TButton").grid(row=2, column=0, columnspan=3, pady=10)
    
    def _create_summary_section(self, parent: ttk.Frame, row: int):
        """Create the summary/statistics section."""
        section_frame = ttk.Frame(parent, padding="2")
        section_frame.grid(row=row, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=2)
        
        # Compact single-line summary
        summary_container = ttk.Frame(section_frame)
        summary_container.pack(fill=tk.X)
        
        self.summary_label = ttk.Label(summary_container, text="No dataset loaded", 
                                       font=("Arial", 9))
        self.summary_label.pack(side=tk.LEFT, padx=5)
        
        ttk.Separator(summary_container, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        self.progress_label = ttk.Label(summary_container, text="Progress: 0 of 0", 
                                       font=("Arial", 9, "bold"))
        self.progress_label.pack(side=tk.LEFT, padx=5)
    
    def _create_main_content_section(self, parent: ttk.Frame, row: int):
        """Create the main content section with image on left and controls on right."""
        # Configure row weight for expansion
        parent.rowconfigure(row, weight=1)
        
        # Left panel - Image display (takes up more space)
        left_panel = ttk.Frame(parent)
        left_panel.grid(row=row, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 5))
        left_panel.rowconfigure(0, weight=1)
        left_panel.columnconfigure(0, weight=1)
        
        self._create_image_section(left_panel)
        
        # Right panel - Detection and Manual Entry (compact)
        right_panel = ttk.Frame(parent)
        right_panel.grid(row=row, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        right_panel.rowconfigure(0, weight=0)  # Detection section - fixed size
        right_panel.rowconfigure(1, weight=1)  # Manual entry - expandable but controlled
        right_panel.columnconfigure(0, weight=1)
        
        self._create_detection_section(right_panel, row=0)
        self._create_manual_entry_section(right_panel, row=1)
    
    def _create_image_section(self, parent: ttk.Frame):
        """Create the image display section."""
        section_frame = ttk.LabelFrame(parent, text="Image Preview", padding="5")
        section_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        section_frame.rowconfigure(0, weight=1)
        section_frame.columnconfigure(0, weight=1)
        
        # Image canvas
        self.image_canvas = tk.Canvas(section_frame, bg='gray')
        self.image_canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Image filename label at bottom
        self.filename_label = ttk.Label(section_frame, text="", font=("Arial", 9, "bold"))
        self.filename_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
    
    def _create_detection_section(self, parent: ttk.Frame, row: int):
        """Create the detection results section."""
        section_frame = ttk.LabelFrame(parent, text="Detected", padding="5")
        section_frame.grid(row=row, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        
        # Compact scrollable frame
        canvas = tk.Canvas(section_frame, height=120)
        scrollbar = ttk.Scrollbar(section_frame, orient="vertical", command=canvas.yview)
        self.detection_frame = ttk.Frame(canvas)
        
        self.detection_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.detection_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.detection_text = ttk.Label(self.detection_frame, text="No detections", 
                                       font=("Arial", 9))
        self.detection_text.pack(anchor=tk.W, padx=2, pady=2)
    
    def _create_manual_entry_section(self, parent: ttk.Frame, row: int):
        """Create the manual entry section."""
        section_frame = ttk.LabelFrame(parent, text="Manual Entry", padding="5")
        section_frame.grid(row=row, column=0, sticky=(tk.W, tk.E))
        
        # Scrollable container for manual entry widgets with limited height
        canvas = tk.Canvas(section_frame, height=250)
        scrollbar = ttk.Scrollbar(section_frame, orient="vertical", command=canvas.yview)
        self.manual_container = ttk.Frame(canvas)
        
        self.manual_container.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.manual_container, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.grid(row=0, column=0, sticky=(tk.W, tk.E))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
    
    def _create_navigation_section(self, parent: ttk.Frame, row: int):
        """Create the navigation and export section."""
        section_frame = ttk.Frame(parent, padding="5")
        section_frame.grid(row=row, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Navigation buttons
        nav_frame = ttk.Frame(section_frame)
        nav_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        self.prev_button = ttk.Button(nav_frame, text="← Previous", command=self._previous_image, 
                                     state=tk.DISABLED)
        self.prev_button.pack(side=tk.LEFT, padx=5)
        
        self.next_button = ttk.Button(nav_frame, text="Next →", command=self._next_image, 
                                     state=tk.DISABLED)
        self.next_button.pack(side=tk.LEFT, padx=5)
        
        self.save_button = ttk.Button(nav_frame, text="Save Current", command=self._save_current, 
                                     state=tk.DISABLED)
        self.save_button.pack(side=tk.LEFT, padx=5)
        
        # Export button
        self.export_button = ttk.Button(section_frame, text="Export to CSV", 
                                       command=self._export_data, state=tk.DISABLED)
        self.export_button.pack(side=tk.RIGHT, padx=5)
    
    def _bind_shortcuts(self):
        """Bind keyboard shortcuts."""
        self.root.bind('<Left>', lambda e: self._previous_image())
        self.root.bind('<Right>', lambda e: self._next_image())
        self.root.bind('<Control-s>', lambda e: self._save_current())
        self.root.bind('<Control-e>', lambda e: self._export_data())
    
    def _browse_folder(self):
        """Browse for results folder."""
        folder = filedialog.askdirectory(title="Select YOLOv8 Results Folder")
        if folder:
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(0, folder)
    
    def _browse_yaml(self):
        """Browse for YAML configuration file."""
        yaml_file = filedialog.askopenfilename(
            title="Select Class Configuration YAML",
            filetypes=[("YAML files", "*.yaml *.yml"), ("All files", "*.*")]
        )
        if yaml_file:
            self.yaml_entry.delete(0, tk.END)
            self.yaml_entry.insert(0, yaml_file)
    
    def _load_dataset(self):
        """Load and validate the dataset."""
        folder_path = self.folder_entry.get()
        yaml_path = self.yaml_entry.get()
        
        if not folder_path:
            messagebox.showerror("Error", "Please select a results folder")
            return
        
        if not yaml_path:
            messagebox.showerror("Error", "Please select a YAML configuration file")
            return
        
        try:
            # Parse YAML
            self.yaml_file = Path(yaml_path)
            yaml_parser = YAMLParser(self.yaml_file)
            self.class_names = yaml_parser.get_class_names()
            
            # Initialize validator
            self.results_folder = Path(folder_path)
            self.validator = InferenceValidator(self.results_folder, self.class_names)
            
            # Get images and validate
            self.images = self.validator.get_image_files()
            
            if not self.images:
                messagebox.showerror("Error", "No images found in the results folder")
                return
            
            # Validate labels
            validation_summary = self.validator.validate_labels()
            
            # Update summary
            self._update_summary(validation_summary)
            
            # Initialize validation data storage
            self.validation_data = [{"processed": False} for _ in self.images]
            
            # Load first image
            self.current_index = 0
            self._load_current_image()
            
            # Enable navigation
            self._update_navigation_buttons()
            self.save_button.config(state=tk.NORMAL)
            self.export_button.config(state=tk.NORMAL)
            
            # Setup manual entry widgets
            self._setup_manual_entry_widgets()
            
            messagebox.showinfo("Success", "Dataset loaded successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load dataset: {str(e)}")
    
    def _update_summary(self, validation_summary: Dict):
        """Update the summary section."""
        total = validation_summary['total_images']
        with_labels = validation_summary['images_with_labels']
        without_labels = validation_summary['images_without_labels']
        
        summary_text = (f"Total: {total} | "
                       f"With Labels: {with_labels} | "
                       f"Without Labels: {without_labels}")
        
        self.summary_label.config(text=summary_text)
        self._update_progress()
    
    def _update_progress(self):
        """Update the progress label."""
        if not self.validation_data:
            return
        
        processed = sum(1 for item in self.validation_data if item.get("processed", False))
        total = len(self.validation_data)
        
        self.progress_label.config(text=f"Progress: {processed} of {total} processed")
    
    def _setup_manual_entry_widgets(self):
        """Setup manual entry widgets for all classes."""
        # Clear existing widgets
        for widget in self.manual_container.winfo_children():
            widget.destroy()
        
        self.manual_entry_widgets.clear()
        
        # Create a compact grid with 2 columns of class entries
        num_classes = len(self.class_names)
        mid_point = (num_classes + 1) // 2
        
        sorted_classes = sorted(self.class_names.items())
        
        # Left column
        for idx, (class_id, class_name) in enumerate(sorted_classes[:mid_point]):
            row = idx
            
            # Truncate long class names
            display_name = class_name if len(class_name) <= 25 else class_name[:22] + "..."
            
            ttk.Label(self.manual_container, text=display_name, font=("Arial", 8)).grid(
                row=row, column=0, padx=2, pady=1, sticky=tk.W)
            
            spinbox = ttk.Spinbox(self.manual_container, from_=0, to=100, width=5)
            spinbox.set(0)
            spinbox.grid(row=row, column=1, padx=2, pady=1, sticky=tk.W)
            
            self.manual_entry_widgets[class_name] = spinbox
        
        # Right column
        for idx, (class_id, class_name) in enumerate(sorted_classes[mid_point:]):
            row = idx
            
            # Truncate long class names
            display_name = class_name if len(class_name) <= 25 else class_name[:22] + "..."
            
            ttk.Label(self.manual_container, text=display_name, font=("Arial", 8)).grid(
                row=row, column=2, padx=2, pady=1, sticky=tk.W)
            
            spinbox = ttk.Spinbox(self.manual_container, from_=0, to=100, width=5)
            spinbox.set(0)
            spinbox.grid(row=row, column=3, padx=2, pady=1, sticky=tk.W)
            
            self.manual_entry_widgets[class_name] = spinbox
    
    def _load_current_image(self):
        """Load and display the current image."""
        if not self.images or self.current_index >= len(self.images):
            return
        
        current_image_path = self.images[self.current_index]
        
        # Update filename label
        self.filename_label.config(text=f"File: {current_image_path.name}")
        
        # Load and display image
        try:
            img = Image.open(current_image_path)
            
            # Resize to fit canvas while maintaining aspect ratio
            canvas_width = self.image_canvas.winfo_width()
            canvas_height = self.image_canvas.winfo_height()
            
            # Use default size if canvas not yet rendered
            if canvas_width <= 1:
                canvas_width = 800
            if canvas_height <= 1:
                canvas_height = 400
            
            img.thumbnail((canvas_width, canvas_height), Image.Resampling.LANCZOS)
            
            photo = ImageTk.PhotoImage(img)
            
            # Clear canvas and display image
            self.image_canvas.delete("all")
            self.image_canvas.create_image(
                canvas_width // 2, canvas_height // 2, 
                image=photo, anchor=tk.CENTER
            )
            
            # Keep a reference to prevent garbage collection
            self.image_canvas.image = photo
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {str(e)}")
        
        # Load detection results
        self._load_detections()
        
        # Load previously saved manual entries if any
        self._load_manual_entries()
        
        # Update navigation
        self._update_navigation_buttons()
        self._update_progress()
    
    def _load_detections(self):
        """Load and display detection results for current image."""
        if not self.validator or self.current_index >= len(self.images):
            return
        
        current_image_path = self.images[self.current_index]
        detections = self.validator.get_detections(current_image_path)
        
        # Clear previous detection display
        for widget in self.detection_frame.winfo_children():
            widget.destroy()
        
        if detections is None:
            # No label file exists
            self.detection_text = ttk.Label(
                self.detection_frame, 
                text="⚠ No label file\nEnter counts manually",
                font=("Arial", 8, "bold"),
                foreground="orange"
            )
            self.detection_text.pack(anchor=tk.W, padx=2, pady=2)
        elif len(detections) == 0:
            # Label file exists but is empty
            self.detection_text = ttk.Label(
                self.detection_frame, 
                text="ℹ No objects detected",
                font=("Arial", 8),
                foreground="blue"
            )
            self.detection_text.pack(anchor=tk.W, padx=2, pady=2)
        else:
            # Display detection counts in compact format
            detection_counts = Counter(detections)
            
            # Create grid for compact display
            for idx, (class_id, count) in enumerate(sorted(detection_counts.items())):
                class_name = self.class_names.get(class_id, f"Unknown ({class_id})")
                # Truncate long names
                display_name = class_name if len(class_name) <= 20 else class_name[:17] + "..."
                
                label = ttk.Label(self.detection_frame, 
                                 text=f"{display_name}: {count}",
                                 font=("Arial", 8))
                label.pack(anchor=tk.W, padx=2, pady=1)
            detection_counts = Counter(detections)
            
            text_parts = ["Detected:"]
            for class_id, count in sorted(detection_counts.items()):
                class_name = self.class_names.get(class_id, f"Unknown ({class_id})")
                text_parts.append(f"  • {class_name}: {count}")
            
            self.detection_text = ttk.Label(
                self.detection_frame, 
                text="\n".join(text_parts),
                font=("Arial", 10),
                foreground="green"
            )
            self.detection_text.pack(anchor=tk.W, padx=5, pady=5)
    
    def _load_manual_entries(self):
        """Load previously saved manual entries for current image."""
        if self.current_index >= len(self.validation_data):
            return
        
        saved_data = self.validation_data[self.current_index]
        
        # Reset all spinboxes first
        for spinbox in self.manual_entry_widgets.values():
            spinbox.set(0)
        
        # Load saved manual entries if any
        if "manual_counts" in saved_data:
            for class_name, count in saved_data["manual_counts"].items():
                if class_name in self.manual_entry_widgets:
                    self.manual_entry_widgets[class_name].set(count)
    
    def _save_current(self):
        """Save the current image's validation data."""
        if self.current_index >= len(self.validation_data):
            return
        
        current_image_path = self.images[self.current_index]
        
        # Get detected counts
        detected_counts = {}
        detections = self.validator.get_detections(current_image_path)
        if detections:
            detection_counter = Counter(detections)
            for class_id, count in detection_counter.items():
                class_name = self.class_names.get(class_id, f"Unknown ({class_id})")
                detected_counts[class_name] = count
        
        # Get manual counts
        manual_counts = {}
        for class_name, spinbox in self.manual_entry_widgets.items():
            count = int(spinbox.get())
            if count > 0:
                manual_counts[class_name] = count
        
        # Save data
        self.validation_data[self.current_index] = {
            "image_name": current_image_path.name,
            "detected_counts": detected_counts,
            "manual_counts": manual_counts,
            "has_label_file": detections is not None,
            "processed": True
        }
        
        self._update_progress()
        
        # Auto-advance to next image
        if self.current_index < len(self.images) - 1:
            self._next_image()
    
    def _previous_image(self):
        """Navigate to previous image."""
        if self.current_index > 0:
            self.current_index -= 1
            self._load_current_image()
    
    def _next_image(self):
        """Navigate to next image."""
        if self.current_index < len(self.images) - 1:
            self.current_index += 1
            self._load_current_image()
    
    def _update_navigation_buttons(self):
        """Update navigation button states."""
        if not self.images:
            return
        
        self.prev_button.config(
            state=tk.NORMAL if self.current_index > 0 else tk.DISABLED
        )
        self.next_button.config(
            state=tk.NORMAL if self.current_index < len(self.images) - 1 else tk.DISABLED
        )
    
    def _export_data(self):
        """Export validation data to CSV."""
        if not self.validation_data:
            messagebox.showwarning("Warning", "No data to export")
            return
        
        # Ask user for save location
        file_path = filedialog.asksaveasfilename(
            title="Save Validation Data",
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if not file_path:
            return
        
        try:
            self.exporter.export_to_csv(self.validation_data, self.class_names, file_path)
            messagebox.showinfo("Success", f"Data exported successfully to:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export data: {str(e)}")


def main():
    """Main entry point."""
    root = tk.Tk()
    
    # Set window size based on screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    window_width = min(1200, int(screen_width * 0.8))
    window_height = min(900, int(screen_height * 0.8))
    
    # Center the window
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    # Create app
    app = YOLOValidatorApp(root)
    
    # Run
    root.mainloop()


if __name__ == "__main__":
    main()
