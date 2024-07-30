import zipfile

to_add = [
    "./Files/SampleTextFile_100kb.txt",
    "./Files/SampleTextFile_50kb.txt"
]

def add_to_zip(zipf, files, option):
    with zipfile.ZipFile(zipf, option) as archive:
        for f in files:
            lst = archive.namelist()
            if not f in lst:
                archive.write(f)
            else:
                print("This file is already in the ZIP.")

add_to_zip("./files.zip", to_add, "a")