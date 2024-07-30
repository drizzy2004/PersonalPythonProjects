import os

def remove_file(src):
    if os.path.isfile(src):
        try: 
            os.remove(src)
        except OSError as e:
            print(f"Error: {src} : {e.strerror}")
        
    else:
        print(f"Error: {src} is not a file.")


remove_file("./Files/gang.txt")