# Python Exceptions Q&A

## Q1. What is the `raise` keyword in Python, and when is it used?

The `raise` keyword in Python is used to manually trigger an exception. It’s helpful when you want to stop program execution or signal an error condition. For example, it’s used to enforce conditions or handle specific cases.

## Q2. How do you use the `raise` keyword to throw a specific exception? Provide an example.

You can raise a specific exception by using `raise` with the exception type and an optional message. Example:

```python
x = -1
if x < 0:
    raise ValueError("x cannot be negative")
```

## Q3. What is the purpose of the `assert` keyword in Python?

The `assert` keyword is used for debugging. It checks if a condition is true, and if false, it raises an `AssertionError`. It’s great for testing assumptions during development.

## Q4. Explain the difference between `raise` and `assert` with examples.

- `raise` manually triggers an exception, e.g., `raise ValueError("Invalid input")`.
- `assert` checks a condition and raises `AssertionError` if false, e.g., `assert x > 0, "x should be positive"`.
  The key difference is `raise` is for explicit error handling, while `assert` is for debugging checks.

## Q5. What are custom exceptions in Python, and why are they useful?

Custom exceptions are user-defined exceptions created by inheriting from the `Exception` class. They’re useful for adding specific error types to make code more readable and manageable in large applications.

## Q6. How do you define and raise a custom exception in Python? Provide an example.

You define a custom exception by creating a class inheriting from `Exception`, then raise it using `raise`. Example:

```python
class CustomError(Exception):
    pass

raise CustomError("This is a custom error")
```

## Q7. Write a Python program to demonstrate the creation and handling of a custom exception.

```python
class CustomError(Exception):
    pass

try:
    age = -5
    if age < 0:
        raise CustomError("Age cannot be negative")
except CustomError as e:
    print(f"Error: {e}")
```

## Q8. What are the advantages of using custom exceptions in large Python applications?

Custom exceptions improve code clarity, allow specific error handling, enhance debugging, and support modular design by isolating error types for different components.
