# Terminal Commands and Python os Module Q&A

## Q1. What are terminal commands, and how are they used in Python programming?

Terminal commands are instructions entered into a command-line interface to interact with the operating system. In Python programming, they are used to execute scripts, manage files, or install packages by running commands like `python script.py` or using the `os` module to execute system commands via `os.system()`.

## Q2. Explain the purpose of the cd, ls (or dir on Windows), and pwd commands in the terminal.

- `cd`: Changes the current directory to a specified one (e.g., `cd /path`).
- `ls` (or `dir` on Windows): Lists files and directories in the current directory.
- `pwd`: Displays the current working directory's full path.

## Q3. How do you create, rename, and delete directories using terminal commands?

- Create: `mkdir new_folder`
- Rename: `mv old_name new_name` (Unix) or `ren old_name new_name` (Windows)
- Delete: `rmdir folder_name` (empty) or `rm -r folder_name` (with content, Unix) / `rd folder_name` (Windows)

## Q4. What are the commands to check Python version and installed packages using the terminal?

- Check Python version: `python --version` or `python -V`
- Check installed packages: `pip list`

## Q5. How do you run a Python script using terminal commands? Provide an example.

Run a script by navigating to its directory and typing: `python script_name.py`. Example: `python hello.py`.

## Q6. Explain how to use terminal commands to redirect output to a file.

Use the `>` operator to redirect output, e.g., `ls > output.txt` (Unix) or `dir > output.txt` (Windows) saves the directory listing to `output.txt`.

## Q7. What is the os module in Python, and why is it important?

The `os` module provides a way to interact with the operating system, allowing file and directory manipulation, path handling, and system command execution. It's important for creating portable, OS-independent Python code.

## Q8. How can you retrieve the current working directory using the os module?

Use `os.getcwd()` to get the current working directory, e.g., `print(os.getcwd())`.

## Q9. Explain the difference between os.mkdir() and os.makedirs() functions with examples.

- `os.mkdir('folder')`: Creates a single directory. Raises an error if the parent doesn't exist.
  Example: `os.mkdir('new_folder')`
- `os.makedirs('parent/child')`: Creates a directory and any necessary parent directories.
  Example: `os.makedirs('parent/child')`

## Q10. How can you list all files and directories in a folder using the os module?

Use `os.listdir(path)` to list contents, e.g., `print(os.listdir('.'))` lists files in the current directory.

## Q11. What is the purpose of os.remove() and os.rmdir()? When should they be used?

- `os.remove('file.txt')`: Deletes a file. Use when removing a specific file.
- `os.rmdir('folder')`: Deletes an empty directory. Use when removing an empty directory only.

## Q12. Provide an example of how to use the os.path module to check if a file or directory exists.

Use `os.path.exists('path')`, e.g., `if os.path.exists('file.txt'): print('Exists!')`.
