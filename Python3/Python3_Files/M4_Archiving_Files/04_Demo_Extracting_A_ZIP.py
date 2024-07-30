import zipfile

def extract_file(zipf, fn, path):
    with zipfile.ZipFile(zipf, "r") as archive:
        archive.extract(fn, path=path)


def extract_all(zipf, path):
    with zipfile.ZipFile(zipf, "r") as archive:
        archive.extractall(path=path)

# extract_file("./files.zip", "Files/SampleCSVFile_11kb.csv", "extracted")
extract_all("./files.zip", "extracted")