# File Organizer Script

## Overview

This Python script automatically organizes files in a specified directory based on their file extensions. It categorizes files into folders such as **Images**, **Documents**, **Videos**, **Music**, **Archives**, and **Code**. Files with unrecognized extensions are moved into an **Uncategorized** folder. This helps keep your downloads or any folder tidy and easier to navigate.

## Features

- Supports multiple file types categorized into relevant folders.
- Automatically creates category folders if they don't exist.
- Moves files into corresponding folders based on their extensions.
- Handles unknown file types by moving them into an **Uncategorized** folder.
- Prints log messages to track file movements.

## Supported File Types

- **Images:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`  
- **Documents:** `.pdf`, `.docx`, `.doc`, `.txt`, `.xlsx`, `.pptx`  
- **Videos:** `.mp4`, `.mkv`, `.mov`, `.avi`  
- **Music:** `.mp3`, `.wav`, `.aac`  
- **Archives:** `.zip`, `.rar`, `.tar`, `.gz`  
- **Code:** `.py`, `.java`, `.cpp`, `.js`, `.html`, `.css`

## Usage

1. Update the `folder_path` variable to the directory you want to organize (e.g., Downloads folder).  
2. Run the script using Python 3.x.  
3. Files will be moved into categorized folders within the specified directory.

Example:

```python
folder_path = r"C:\Users\YourUserName\Downloads"
