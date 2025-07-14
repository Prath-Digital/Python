# Python Functions Guide

## Q1: What are built-in functions in Python? Provide examples of three commonly used built-in functions.
Built-in functions are pre-defined functions in Python that you can use right away. Three commonly used ones are:
- `print()` - Displays output.
- `len()` - Gets the length of an object.
- `range()` - Creates a sequence of numbers.

## Q2: What are user-defined functions (UDF) in Python, and how do they differ from built-in functions?
User-defined functions (UDFs) are functions created by the user using the `def` keyword to perform specific tasks. Unlike built-in functions, which come with Python, UDFs are custom-made, offering tailored functionality.

## Q3: Write a program to create a user-defined function that calculates the factorial of a number.
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print(f"The factorial of {num} is {factorial(num)}")
# Output: The factorial of 5 is 120
```

## Q4: Explain the importance of the return statement in user-defined functions with an example.
The `return` statement sends a value back to where the function was called, ending its execution. Without it, the function won’t provide a usable result. Example:
```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # Output: 7
```

## Q5: Discuss the advantages of using functions in Python programs.
Functions make code reusable, easier to read, and simpler to debug. They break down complex tasks into manageable chunks, saving time and effort.

## Q6: What is the purpose of arbitrary arguments (*args) in Python? Write an example to demonstrate their use.
`*args` allows a function to accept any number of arguments, packed into a tuple, offering flexibility. Example:
```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # Output: 10
```

## Q7: Explain how keyword arguments (**kwargs) work in Python. Provide an example.
`**kwargs` allows a function to accept any number of keyword arguments, stored as a dictionary, ideal for named parameters. Example:
```python
def greet(**kwargs):
    if 'name' in kwargs:
        print(f"Hello, {kwargs['name']}!")

greet(name="Alice")  # Output: Hello, Alice!
```

## Q8: What is the difference between *args and **kwargs in Python? When would you use each?
`*args` handles an arbitrary number of positional arguments (as a tuple), while `**kwargs` handles keyword arguments (as a dictionary). Use `*args` for multiple unnamed inputs (e.g., numbers) and `**kwargs` for named parameters (e.g., options).

## Q9: Write a function using *args and **kwargs to accept multiple arguments and keyword arguments.
```python
def my_function(*args, **kwargs):
    print("Positional args:", args)
    print("Keyword args:", kwargs)

my_function(1, 2, 3, name="Bob", age=25)
# Output: Positional args: (1, 2, 3)
#         Keyword args: {'name': 'Bob', 'age': 25}
```

## Q10: What is the __doc__ attribute in Python, and how can it be used to document functions? Write a Python program that includes a function with a docstring and uses __doc__ to display the function’s documentation.
The `__doc__` attribute stores a function’s docstring, which documents its purpose. Example:
```python
def multiply(a, b):
    """Multiplies two numbers and returns the result."""
    return a * b

print(multiply.__doc__)  # Output: Multiplies two numbers and returns the result.
print(multiply(3, 4))    # Output: 12
```

## Q11: How does Python prioritize arguments when using positional arguments, keyword arguments, *args, and **kwargs together?
Python prioritizes arguments in this order: positional arguments, keyword arguments, `*args`, and `**kwargs`. Example:
```python
def example(pos1, pos2, *args, kw1="default", **kwargs):
    print(f"Positional: {pos1}, {pos2}")
    print(f"Args: {args}")
    print(f"Keyword: {kw1}")
    print(f"Kwargs: {kwargs}")

example(1, 2, 3, 4, kw1="custom", kw2="extra")
# Output:
# Positional: 1, 2
# Args: (3, 4)
# Keyword: custom
# Kwargs: {'kw2': 'extra'}
```