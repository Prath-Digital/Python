# Python Type Casting and Related Concepts

## Q.1 What is type casting in Python, and why is it used? Explain the difference between implicit type casting and explicit type casting with examples.

Type casting in Python is the process of converting a variable from one data type to another. It is used to ensure compatibility between different data types during operations, to meet function or method requirements, or to format data appropriately for processing or display.

### Implicit Type Casting

- Python automatically converts one data type to another without explicit instruction.
- Typically occurs when Python tries to avoid data loss in operations (e.g., converting an integer to a float).
- Example:
  ```python
  x = 5      # Integer
  y = 2.5    # Float
  z = x + y  # Python implicitly converts x to float
  print(z)   # Output: 7.5
  print(type(z))  # Output: <class 'float'>
  ```

### Explicit Type Casting

- The programmer manually converts one data type to another using type-casting constructors.
- Necessary when specific data types are required or to control the conversion process.
- Example:
  ```python
  x = "10"      # String
  y = int(x)    # Explicitly convert string to integer
  print(y + 5)  # Output: 15
  print(type(y))  # Output: <class 'int'>
  ```

## Q.2 What are type-casting constructors? List some commonly used type-casting constructors in Python.

Type-casting constructors are built-in Python functions used to explicitly convert a value from one data type to another.

### Commonly Used Type-Casting Constructors:

- `int()`: Converts to an integer.
- `float()`: Converts to a floating-point number.
- `str()`: Converts to a string.
- `bool()`: Converts to a boolean.
- `complex()`: Converts to a complex number.
- `list()`: Converts to a list.
- `tuple()`: Converts to a tuple.
- `set()`: Converts to a set.
- `dict()`: Converts to a dictionary (requires a specific format, e.g., list of key-value pairs).

## Q.3 What happens if you use int() on a string containing non-numeric characters?

Using `int()` on a string containing non-numeric characters raises a `ValueError` because Python cannot convert non-numeric strings to integers.

Example:

```python
x = "123abc"
y = int(x)  # Raises ValueError: invalid literal for int() with base 10: '123abc'
```

However, `int()` works if the string represents a valid integer:

```python
x = "123"
y = int(x)  # Output: 123
print(y, type(y))  # Output: 123 <class 'int'>
```

## Q.4 What is the purpose of the str() constructor? Provide examples of converting numeric types to strings.

The `str()` constructor converts a value (e.g., numeric types) to a string, often used for concatenation, display, or formatting purposes.

Examples:

```python
# Converting integer to string
num1 = 42
str1 = str(num1)
print(str1 + " is a number")  # Output: 42 is a number
print(type(str1))  # Output: <class 'str'>

# Converting float to string
num2 = 3.14
str2 = str(num2)
print(str2 + " is pi")  # Output: 3.14 is pi
print(type(str2))  # Output: <class 'str'>
```

## Q.5 Write a Python program that demonstrates the use of int(), float(), str(), bool(), and complex() constructors.

```python
# Program demonstrating type-casting constructors
def type_casting_demo():
    # Original values
    str_num = "123"
    int_num = 42
    float_num = 3.14
    bool_val = True
    complex_val = "1+2j"

    # int() constructor
    int_from_str = int(str_num)
    print(f"String '{str_num}' to int: {int_from_str}, Type: {type(int_from_str)}")

    # float() constructor
    float_from_int = float(int_num)
    print(f"Integer {int_num} to float: {float_from_int}, Type: {type(float_from_int)}")

    # str() constructor
    str_from_float = str(float_num)
    print(f"Float {float_num} to string: '{str_from_float}', Type: {type(str_from_float)}")

    # bool() constructor
    bool_from_int = bool(int_num)
    print(f"Integer {int_num} to bool: {bool_from_int}, Type: {type(bool_from_int)}")

    # complex() constructor
    complex_from_str = complex(complex_val)
    print(f"String '{complex_val}' to complex: {complex_from_str}, Type: {type(complex_from_str)}")

type_casting_demo()
```

Output:

```
String '123' to int: 123, Type: <class 'int'>
Integer 42 to float: 42.0, Type: <class 'float'>
Float 3.14 to string: '3.14', Type: <class 'str'>
Integer 42 to bool: True, Type: <class 'bool'>
String '1+2j' to complex: (1+2j), Type: <class 'complex'>
```

## Q.6 What is the purpose of the id() function in Python? Explain how the id() function can be used to verify the identity of an object.

The `id()` function returns a unique identifier for an object, which is an integer representing the object's memory address during its lifetime. It is used to verify whether two variables reference the same object in memory.

Example:

```python
x = 42
y = 42
print(id(x))  # Same id as y (small integers are interned in Python)
print(id(y))  # Same id as x
print(x is y)  # Output: True (same object)

z = [1, 2, 3]
w = [1, 2, 3]
print(id(z))  # Different id from w
print(id(w))  # Different id from z
print(z is w)  # Output: False (different objects)
```

The `id()` function helps confirm object identity, especially when checking if variables point to the same object or distinct objects with the same value.

## Q.7 Write a Python program to demonstrate how the id() function changes when a variable is reassigned.

```python
# Program demonstrating id() function with variable reassignment
def id_demo():
    # Initial assignment
    x = 100
    print(f"Initial x value: {x}, ID: {id(x)}")

    # Reassign x to a new integer
    x = 200
    print(f"Reassigned x value: {x}, ID: {id(x)}")  # New ID

    # Reassign x to a list
    x = [1, 2, 3]
    print(f"Reassigned x to list: {x}, ID: {id(x)}")  # New ID

    # Modify list in place (same object, same ID)
    x.append(4)
    print(f"Modified list x: {x}, ID: {id(x)}")  # Same ID as previous

id_demo()
```

Output (IDs will vary):

```
Initial x value: 100, ID: 140735123456789
Reassigned x value: 200, ID: 140735123459876
Reassigned x to list: [1, 2, 3], ID: 140735987654321
Modified list x: [1, 2, 3, 4], ID: 140735987654321
```

Explanation: Reassigning a variable to a new value creates a new object with a different ID, but modifying a mutable object (e.g., a list) in place retains the same ID.

## Q.8 What does the type() function do in Python? How can the type() function be used to check the data type of a variable? Provide examples.

The `type()` function returns the data type of a variable or object, allowing you to inspect the type during runtime.

Examples:

```python
# Checking data types with type()
x = 42
y = 3.14
z = "Hello"
w = [1, 2, 3]
v = True

print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(z))  # Output: <class 'str'>
print(type(w))  # Output: <class 'list'>
print(type(v))  # Output: <class 'bool'>
```

The `type()` function is useful for debugging, validating inputs, or ensuring variables are of the expected type before performing operations.
