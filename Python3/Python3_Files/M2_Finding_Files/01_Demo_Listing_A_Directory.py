import os

def list_dir(folder):
    print("Files Names:")
    print("------------------------")
    for file_name in os.listdir(folder):
        print(file_name)
    print("------------------------")
list_dir("./Files")