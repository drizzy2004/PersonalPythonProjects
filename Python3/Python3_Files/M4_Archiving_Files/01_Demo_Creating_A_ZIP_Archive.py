import zipfile

files_to_zip = [
    "./Files/SampleCSVFile_11kb.csv",
    "./Files/SampleCSVFile_119kb.csv",
    "./Files/SampleTextFile_10kb.txt",
    "./Files/SampleTextFile_20kb.txt",
]

def create_zip(zipf, files, option):
    with zipfile.ZipFile(zipf, option, allowZip64=True) as archive:
        for f in files:
            archive.write(f)

create_zip("./files.zip", files_to_zip, "w")
