import os

def traverse(folder):
    for folder_path, dirs, files in os.walk(folder):
        print(f"Folder: {folder_path}")
        for file_name in files:
            print(f"\t{file_name}")

traverse("./Files")