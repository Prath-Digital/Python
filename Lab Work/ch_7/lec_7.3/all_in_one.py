import os

def menu():
    print("\nFile and Directory Operations Menu:")
    print("1. Print current working directory")
    print("2. List all files and directories in current folder")
    print("3. Create and manage a file (create, rename, delete)")
    print("4. Create and check a directory")
    print("5. List all files and directories in a given path")
    print("6. Create, rename, and delete an empty file")
    print("7. Fetch and print environment variables")
    print("8. Check if a file or directory exists at a given path")
    print("9. Determine if a path points to a file or directory")
    print("10. Find the size of a file")
    print("11. Copy content of one file to another")
    print("0. Exit")
    return input("Enter your choice (0-11): ")

def execute_terminal_commands():
    os.system("echo Hello from Terminal")
    os.system("echo > sample.txt")
    os.system("del sample.txt" if os.name == 'nt' else "rm sample.txt")

def q3_program():
    print(os.getcwd())
    os.chdir("practice_tasks")
    print("Changed to:", os.getcwd())

def q4_program():
    folder_name = "my_folder"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name) if not os.path.exists(folder_name) else print(f"{folder_name} already exists")
    else:
        print(f"{folder_name} exists")

def q5_program():
    path = input("Enter path to list files and directories: ")
    print(os.listdir(path) if os.path.exists(path) else "Path does not exist")

def q6_program():
    with open("example.txt", "w") as f:
        pass
    os.rename("example.txt", "new_example.txt")
    os.remove("new_example.txt") if os.path.exists("new_example.txt") else print("File not found")

def q7_program():
    print(os.environ)

def q8_program():
    path = input("Enter path to check: ")
    print(os.path.exists(path))

def q9_program():
    path = input("Enter path to check: ")
    if os.path.isfile(path):
        print("Path points to a file")
    elif os.path.isdir(path):
        print("Path points to a directory")
    else:
        print("Path does not exist")

def q10_program():
    path = input("Enter file path to find size: ")
    if os.path.isfile(path):
        print(f"File size: {os.path.getsize(path)} bytes")
    else:
        print("Not a valid file")

def q11_program():
    src = input("Enter source file path: ")
    dest = input("Enter destination file path: ")
    if os.path.isfile(src):
        with open(src, 'r') as f_src, open(dest, 'w') as f_dest:
            f_dest.write(f_src.read())
        print("File content copied successfully")
    else:
        print("Source file does not exist")

while True:
    choice = menu()
    if choice == '1':
        print(os.getcwd())
    elif choice == '2':
        print(os.listdir())
    elif choice == '3':
        execute_terminal_commands()
        q3_program()
    elif choice == '4':
        q4_program()
    elif choice == '5':
        q5_program()
    elif choice == '6':
        q6_program()
    elif choice == '7':
        q7_program()
    elif choice == '8':
        q8_program()
    elif choice == '9':
        q9_program()
    elif choice == '10':
        q10_program()
    elif choice == '11':
        q11_program()
    elif choice == '0':
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again!")