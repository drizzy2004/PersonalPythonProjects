import shutil 

def mv_files(src, dst):
    shutil.move(src, dst)

# mv_files("./Files/SampleCSVFile_2kb.csv", "./Files/Subfolder/SampleCSVFile_2kb.csv")
# mv_files("./Files", "./xyz")

mv_files("./xyz", "./Files")
