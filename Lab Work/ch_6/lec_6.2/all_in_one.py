def divide_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 / num2
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
    except ValueError:
        print("Error: Please enter valid numbers!")

def access_list_element():
    try:
        my_list = [1, 2, 3]
        index = int(input("Enter index to access: "))
        result = my_list[index]
        print(f"Element at index {index}: {result}")
    except IndexError:
        print("Error: Index out of range!")
    except ValueError:
        print("Error: Please enter a valid index!")

def read_file_content():
    try:
        filename = input("Enter filename: ")
        with open(filename, 'r') as file:
            content = file.read()
        print("File content:", content)
    except FileNotFoundError:
        print("Error: File not found!")
    else:
        print("File read successfully!")
    finally:
        print("File operation completed.")

def access_string_element():
    try:
        my_string = "Hello"
        index = int(input("Enter index to access: "))
        result = my_string[index]
        print(f"Character at index {index}: {result}")
    except IndexError:
        print("Error: Index out of range!")
    except ValueError:
        print("Error: Please enter a valid index!")
    else:
        print("Access successful!")

def open_and_close_file():
    try:
        filename = input("Enter filename: ")
        with open(filename, 'r') as file:
            content = file.read()
        print("File content:", content)
    except FileNotFoundError:
        print("Error: File not found!")
    finally:
        print("File is closed.")

def perform_division():
    try:
        num1 = float(input("Enter numerator: "))
        num2 = float(input("Enter denominator: "))
        result = num1 / num2
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
    except ValueError:
        print("Error: Please enter valid numbers!")
    finally:
        print("Operation completed.")

def calculate_square_root():
    try:
        number = float(input("Enter a number: "))
        if number < 0:
            raise ValueError("Cannot calculate square root of a negative number!")
        result = number ** 0.5
        print(f"Square root: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print("Square root calculation successful!")
    finally:
        print("Execution complete.")

while True:
    print("\nMenu:")
    print("1. Divide two numbers")
    print("2. Access list element")
    print("3. Read file content")
    print("4. Access string element")
    print("5. Open and close file")
    print("6. Perform division with final message")
    print("7. Calculate square root")
    print("0. Exit")
    
    choice = input("Enter your choice (0-7): ")
    
    if choice == '1':
        divide_numbers()
    elif choice == '2':
        access_list_element()
    elif choice == '3':
        read_file_content()
    elif choice == '4':
        access_string_element()
    elif choice == '5':
        open_and_close_file()
    elif choice == '6':
        perform_division()
    elif choice == '7':
        calculate_square_root()
    elif choice == '0':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")