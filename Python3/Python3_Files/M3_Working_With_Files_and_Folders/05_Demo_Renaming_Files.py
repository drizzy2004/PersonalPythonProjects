import os
from pathlib import Path

def rename_file_1(source, dest):
    os.rename(source, dest)

def rename_file_2(src, dest):
    f = Path(src)
    f.rename(dest)


# rename_file_1("./Files/SampleCSVFile_11kb.csv", "./Files/gang_gang.csv")
rename_file_2("./Files/gang_gang.csv", "./Files/SampleCSVFile_11kb.csv")
