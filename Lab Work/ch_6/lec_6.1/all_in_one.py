def q1():
    filename = input("Enter filename to write: ")
    with open(filename, "w") as file:
        file.write("Python is a versatile programming language.")

def q2():
    filename = input("Enter filename to overwrite: ")
    with open(filename, "w") as file:
        file.write("Learning file handling in Python is fun!")

def q3():
    filename = input("Enter filename to read: ")
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())

def q4():
    filename = input("Enter filename to write multiple lines: ")
    with open(filename, "w") as file:
        file.write("Line 1: Python is easy to learn.\n")
        file.write("Line 2: It has numerous libraries.\n")
        file.write("Line 3: File handling is one of its features.\n")

def q5():
    filename = input("Enter filename to append: ")
    with open(filename, "a") as file:
        file.write("Line 4: Python supports multiple modes of file handling.\n")

def q6():
    filename = input("Enter filename to read in binary: ")
    with open(filename, "rb") as file:
        content = file.read()
        print(content)

def q7():
    filename = input("Enter filename to analyze: ")
    with open(filename, "r") as file:
        text = file.read()
        words = text.split()
        chars = len(text)
        lines = len(text.split('\n'))
        print(f"Words: {len(words)}, Characters: {chars}, Lines: {lines}")

def q8():
    filename = input("Enter filename to read and append: ")
    with open(filename, "r+") as file:
        content = file.read()
        file.write("\nThis file was last modified by adding this sentence.")

def q9():
    filename = input("Enter filename to search: ")
    search_word = input("Enter word to search: ")
    line_num = 1
    found = False
    with open(filename, "r") as file:
        for line in file:
            if search_word in line:
                print(f"Found at line {line_num}")
                found = True
            line_num += 1
    if not found:
        print("Word not found.")

def q10():
    source_file = input("Enter source filename: ")
    backup_file = input("Enter backup filename: ")
    with open(source_file, "r") as source, open(backup_file, "w") as backup:
        backup.write(source.read())

def q11():
    filename = input("Enter filename to demonstrate modes: ")
    mode = input("Enter mode (r, w, a, r+, rb): ")
    if mode == "r":
        with open(filename, "r") as file:
            print(file.read())
    elif mode == "w":
        with open(filename, "w") as file:
            file.write(input("Enter content: "))
    elif mode == "a":
        with open(filename, "a") as file:
            file.write(input("Enter content to append: "))
    elif mode == "r+":
        with open(filename, "r+") as file:
            print(file.read())
            file.write(input("Enter content to add: "))
    elif mode == "rb":
        with open(filename, "rb") as file:
            print(file.read())
    else:
        print("Invalid mode!")
    print("File closed.")

while True:
    print("\nMenu:")
    print("1. Write to a file")
    print("2. Overwrite a file")
    print("3. Read a file line by line")
    print("4. Write multiple lines to a file")
    print("5. Append to a file")
    print("6. Read a file in binary mode")
    print("7. Count words, characters, lines in a file")
    print("8. Read and append to a file")
    print("9. Search word in a file")
    print("10. Copy from one file to another")
    print("11. Demonstrate all modes")
    print("0. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        q1()
    elif choice == 2:
        q2()
    elif choice == 3:
        q3()
    elif choice == 4:
        q4()
    elif choice == 5:
        q5()
    elif choice == 6:
        q6()
    elif choice == 7:
        q7()
    elif choice == 8:
        q8()
    elif choice == 9:
        q9()
    elif choice == 10:
        q10()
    elif choice == 11:
        q11()
    elif choice == 0:
        break
    else:
        print("Invalid choice! Please try again.")