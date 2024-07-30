import shutil

def copy_file(src, dst):
    shutil.copy(src, dst)

def copy_folder(src, dst):
    shutil.copytree(src, dst)

# copy_file("./Files/SampleCSVFile_2kb.csv", "./Files/Subfolder")

copy_folder("./Files/Subfolder", "./Files/new_folder")