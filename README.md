# HyperSoft

HyperSoft is a simple Python application that rotates your desktop wallpaper based on a user-defined schedule and an image collection stored in a specific folder on Windows systems.

## Features

- Automatically changes the desktop wallpaper at regular intervals.
- Supports various image formats including PNG, JPG, JPEG, BMP, and TIFF.
- Runs in the background and updates the wallpaper without interrupting your workflow.

## Requirements

- Python 3.x
- Windows operating system

## Installation

1. Clone the repository or download the `hypersoft.py` file.
2. Ensure you have Python installed on your system.
3. Install any required dependencies if necessary (none for basic operation).

## Usage

1. Update the `image_folder` variable in `hypersoft.py` with the path to your image collection folder.
2. Set the `interval_seconds` variable to define how often you want the wallpaper to change (in seconds).
3. Run the script using Python:

   ```bash
   python hypersoft.py
   ```

4. The application will start and run in the background, changing your wallpaper at the specified intervals.

## Customization

- You can modify the image formats supported by editing the file extensions in the `_load_images` method.
- Adjust the schedule by changing the `interval_seconds` variable value.

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project is licensed under the MIT License.