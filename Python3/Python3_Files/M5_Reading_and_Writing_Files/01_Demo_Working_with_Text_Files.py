
def read_text(filename):
    with open(filename) as f:
        print(f.read())

def read_text_by_line(filename):
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            print(line, end="")
            line = f.readline()

def write_new_txt(filename, str):
    with open(filename, "w", encoding = "utf-8") as f:
        f.write(str)

def append_new_line(filename, str):
    with open(filename, "a", encoding = "utf-8") as f:
        f.write("\n")
        f.write(str)

# read_text("./Files/SampleTextFile_10kb.txt")
# read_text_by_line("./Files/SampleTextFile_10kb.txt")
# write_new_txt("./Files/example.txt", "I want to be a software engineer")
append_new_line("./Files/SampleTextFile_10kb.txt", "I want to become a great engineer")


