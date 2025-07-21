# File Handling in Python Q&A

## Q1. What is file handling in Python, and why is it important?
File handling in Python refers to the process of managing files, including creating, reading, updating, and deleting them. It is important because it allows programs to store data permanently, interact with external data sources, and perform tasks like data analysis or logging.

## Q2. Explain the difference between text and binary files in Python.
Text files store data as readable characters (e.g., .txt files), while binary files store data in a format that is not human-readable (e.g., .jpg, .exe). Text files use encoding like UTF-8, whereas binary files preserve raw data. Example: A .txt file with "Hello" vs. a .png image file.

## Q3. How do you open a file for reading and writing in Python? Provide examples.
To open a file for reading, use `open('file.txt', 'r')`. For writing, use `open('file.txt', 'w')`. Example for reading:
```python
with open('file.txt', 'r') as file:
    content = file.read()
```
Example for writing:
```python
with open('file.txt', 'w') as file:
    file.write('Hello, World!')
```

## Q4. Write a Python program to read a text file line by line and display its content.
```python
with open('file.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

## Q5. What are the different modes of opening a file in Python, such as 'r', 'w', 'a', and 'x'?
- 'r': Read (default mode).
- 'w': Write (overwrites or creates a file).
- 'a': Append (adds to the end of a file).
- 'x': Exclusive creation (fails if file exists).

## Q6. Explain the purpose of the 'b' and 't' modes when opening files.
- 'b': Binary mode, used for non-text files (e.g., images).
- 't': Text mode (default), used for text files. Example: `open('file.bin', 'rb')` for binary reading.

## Q7. How does the '+' mode enhance file operations? Provide examples.
The '+' mode allows both reading and writing. Example: `open('file.txt', 'r+')` reads and writes to an existing file. Another example: `open('file.txt', 'w+')` creates or overwrites a file and allows reading.

## Q8. How do you write data to a text file in Python? Provide an example.
```python
with open('file.txt', 'w') as file:
    file.write('This is a test line.\n')
```

## Q9. Explain the difference between `read()`, `readline()`, and `readlines()` methods in Python.
- `read()`: Reads the entire file content as a single string.
- `readline()`: Reads a single line at a time.
- `readlines()`: Reads all lines into a list. Example:
```python
with open('file.txt', 'r') as file:
    print(file.read())  # Entire content
    print(file.readline())  # First line
    print(file.readlines())  # List of all lines
```

## Q10. Write a Python program to append data to an existing file and read its content.
```python
with open('file.txt', 'a') as file:
    file.write('New line added.\n')
with open('file.txt', 'r') as file:
    print(file.read())
```

## Q11. What is the importance of closing a file in Python, and how is it done programmatically?
Closing a file is important to free up system resources and ensure data is fully written. It is done using `file.close()` or preferably with a `with` statement, which automatically closes the file.