import os, fnmatch

def match(folder, search_phrase):
    for file_name in os.listdir(folder):
        if fnmatch.fnmatch(file_name, search_phrase):
            print(file_name)

# match("./Files", "*_1*.*")
match("./Files", "*_2*.*")