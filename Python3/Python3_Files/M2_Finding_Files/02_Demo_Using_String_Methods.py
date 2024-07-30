import os

def ends_with(folder, search_phrase):
    print("------------------------")
    for file_name in os.listdir(folder):
        if file_name.endswith(search_phrase):
            print(file_name)
    print("------------------------")

def starts_with(folder, search_phrase):
    print("------------------------")
    for file_name in os.listdir(folder):
        if file_name.startswith(search_phrase):
            print(file_name) 
    print("------------------------")

ends_with("./Files", ".txt")
starts_with("./Files", "Sample")

