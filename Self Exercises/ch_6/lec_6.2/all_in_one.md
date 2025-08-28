# Python Exception Handling Q&A

## Q1: What is an exception in Python, and how does it differ from an error?
An exception in Python is an event that disrupts the normal flow of a program due to unexpected conditions (e.g., division by zero). It differs from an error in that exceptions can be handled with try-except blocks, allowing the program to recover, while errors (e.g., syntax errors) typically halt execution and require code correction.

## Q2: List some common built-in exceptions in Python and briefly describe their purpose.
- **ZeroDivisionError**: Raised when dividing a number by zero.
- **FileNotFoundError**: Occurs when a file or directory is requested but doesn’t exist.
- **ValueError**: Triggered when a function gets an argument of the right type but an invalid value.
- **TypeError**: Raised when an operation is performed on an incompatible type.
- **IndexError**: Occurs when trying to access an index that is out of range in a list or tuple.

## Q3: Why is exception handling important in programming?
Exception handling is crucial because it prevents programs from crashing due to unforeseen issues, allows graceful error recovery, improves user experience by providing meaningful feedback, and ensures robust code that can handle unexpected inputs or conditions.

## Q4: What is the purpose of the try and except blocks in Python?
The `try` block contains code that might raise an exception, while the `except` block handles the exception if it occurs, allowing the program to continue running or respond appropriately instead of terminating.

## Q5: Write a Python program to handle a ZeroDivisionError using try ... except.
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
```

## Q6: Can a single try block have multiple except blocks? If yes, explain with an example.
Yes, a single `try` block can have multiple `except` blocks to handle different exceptions.  
```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid number!")
```

## Q7: What is the role of the else block in a try ... except construct?
The `else` block executes if no exception occurs in the `try` block, providing a way to run code that should only run under normal conditions.

## Q8: Write a Python program demonstrating the use of try ... except ... else for handling file operations.
```python
try:
    file = open("example.txt", "r")
except FileNotFoundError:
    print("Error: File not found!")
else:
    content = file.read()
    print("File content:", content)
    file.close()
```

## Q9: What is the purpose of the finally block in Python exception handling?
The `finally` block executes regardless of whether an exception occurred, making it ideal for cleanup actions like closing files or releasing resources.

## Q10: Write a Python program to demonstrate try ... except ... finally where the finally block executes cleanup code.
```python
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Error: File not found!")
finally:
    print("Cleanup: Closing the file.")
    try:
        file.close()
    except NameError:
        pass
```

## Q11: Can the try block have all except, else, and finally blocks together? If yes, explain their sequence of execution with an example.
Yes, a `try` block can include all `except`, `else`, and `finally` blocks. The sequence is: `try` block runs first, `except` handles any exceptions, `else` runs if no exception occurs, and `finally` always runs last.  
```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid number!")
else:
    print("Result:", result)
finally:
    print("Execution complete!")
```

## Q12: Write a Python program that uses all four blocks (try, except, else, and finally) in a real-world scenario, such as processing user input or handling file operations.
```python
try:
    file = open("data.txt", "r")
    num = int(input("Enter a number to divide file size by: "))
    size = len(file.read())
    result = size / num
except FileNotFoundError:
    print("Error: Data file not found!")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid number!")
else:
    print("Division result:", result)
finally:
    print("Cleanup: Closing the file.")
    try:
        file.close()
    except NameError:
        pass
```