def find_acronym():
    look_up = input("What software acronym do you want to look up?\n")

    found = False
    try:
        with open("sftw_input.txt") as f:
            for line in f:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print("File not found")
        return

    if not found: 
        print("The acronym doesn't exist")

def add_acronym():
    # Ask the user what acronym they want to add
    acronym = input("What acronym do you want to add?\n")

    # Then ask the user for the definition
    definition = input("What is the definition?\n")

    # Open the file
    with open("input.txt", "a") as f:
        f.write(acronym + " - " + definition + "\n")

def main():
    choice = input("Do you want to find(F) or add(A) an acronym?\n")

    if choice == "F":
        find_acronym()
    elif choice == "A":
        add_acronym()
    else: 
        print("Not a valid choice")

main()
            

