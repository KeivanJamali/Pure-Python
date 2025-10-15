# Elevation Data Processor App

This is a PyQt5-based Windows application for processing and visualizing elevation data using the logic from `main.py`.

## Features
- Select CSV data file
- Set time and elevation thresholds
- Process and group data
- View and plot group statistics
- Save processed and removed notes data

## How to Run
1. Make sure you have Python 3 and the required packages installed:
   - PyQt5
   - pandas
   - matplotlib
2. Run the app:
   ```bash
   python main_window.py
   ```

## Folder Structure
- `main_window.py`: Main PyQt5 application
- `main.py`: Data processing logic (used by the app)

## Notes
- The app uses the same logic as the notebook and CLI usage in `main.py`.
- Output files are saved in the selected directory.
