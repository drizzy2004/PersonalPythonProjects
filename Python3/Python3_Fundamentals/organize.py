import os
import shutil
from pathlib import Path

def organize_desktop():
    # Path to the user's desktop
    desktop_path = Path.home() / 'Desktop'

    # Dictionary mapping file extensions to folder names
    folders = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
        "Files": [".txt", ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"]
    }

    # Create folders if they don't exist
    for folder_name in folders:
        folder_path = desktop_path / folder_name
        folder_path.mkdir(exist_ok=True)

    # Iterate over files on desktop and move them to respective folders
    for file_name in desktop_path.iterdir():
        file_path = os.path.join(desktop_path, file_name)
        if os.path.isfile(file_path):
            for folder_name, extensions in folders.items():
                    if file_name.suffix.lower() in extensions:
                        destination_folder = os.path.join(desktop_path, folder_name)
                        shutil.move(str(file_path), str(destination_folder))

    print("Desktop files organized successfully!")

# Run the function to organize desktop files
if __name__ == "__main__":
    organize_desktop()
