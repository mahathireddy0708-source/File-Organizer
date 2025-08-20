import os
import shutil

# Define categories with extensions
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Code": [".py", ".java", ".cpp", ".js", ".html", ".css"]
}

# *** IMPORTANT: Change this to your actual folder path ***
folder_path = r"C:\Users\rise\Downloads"  # <-- replace 'rise' with your Windows username or your folder

# Create category folders if they don't exist
for category in file_types.keys():
    category_path = os.path.join(folder_path, category)
    try:
        os.makedirs(category_path, exist_ok=True)
    except PermissionError:
        print(f"Permission denied: cannot create folder {category_path}")

# Create Uncategorized folder path
uncategorized = os.path.join(folder_path, "Uncategorized")
try:
    os.makedirs(uncategorized, exist_ok=True)
except PermissionError:
    print(f"Permission denied: cannot create folder {uncategorized}")

# Organize files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    # Skip directories and hidden files
    if os.path.isdir(file_path) or file.startswith('.'):
        continue

    file_ext = os.path.splitext(file)[1].lower()
    moved = False

    for category, extensions in file_types.items():
        if file_ext in extensions:
            dest_path = os.path.join(folder_path, category, file)
            try:
                shutil.move(file_path, dest_path)
                print(f"Moved: {file} --> {category}")
            except PermissionError:
                print(f"Permission denied: cannot move file {file}")
            moved = True
            break

    if not moved:
        dest_path = os.path.join(uncategorized, file)
        try:
            shutil.move(file_path, dest_path)
            print(f"Moved: {file} --> Uncategorized")
        except PermissionError:
            print(f"Permission denied: cannot move file {file}")

print("✅ Files organized successfully!")
