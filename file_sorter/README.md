# Auto Sort Downloads

## Overview
This script automatically organizes files in the `Downloads` folder by sorting them into categorized subfolders based on their file extensions. It helps keep the `Downloads` directory tidy and makes it easier to locate files.

## How It Works
1. The script scans the `Downloads` folder.
2. It checks the file extensions and matches them to predefined categories.
3. If a file belongs to a category, it is moved to the corresponding folder.
4. If a file does not match any category, it is placed in an `Others` folder.
5. If a file with the same name already exists in the destination folder, a unique name is generated to prevent overwriting.

## Supported Categories
- **PDFs** (`.pdf`)
- **Images** (`.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`)
- **ZIP Files** (`.zip`, `.rar`, `.7z`, `.tar`, `.gz`)
- **Executables** (`.exe`, `.msi`, `.bat`)
- **Documents** (`.doc`, `.docx`, `.txt`, `.odt`, `.rtf`)
- **Videos** (`.mp4`, `.mkv`, `.avi`, `.mov`)

## Installation & Usage
1. **Ensure Python is installed**
   - Check by running: `python --version`
2. **Download or clone the script**
3. **Run the script**
   ```sh
   python auto_sort_downloads.py
   ```

## Customization
- Modify the `FILE_TYPES` dictionary in the script to add or change file categories.
- Change the `downloads_folder` variable if your downloads are stored in a different location.

## Notes
- The script skips directories and only processes files.
- It creates folders dynamically if they do not exist.
- Errors are handled to prevent interruptions.

## License
This script is free to use and modify.

