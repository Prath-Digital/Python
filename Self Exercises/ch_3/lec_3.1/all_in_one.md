# Python Concepts and Programs

## Q1: What is string formatting in Python, and how do the format() method and f-strings differ? Provide examples.
String formatting in Python allows embedding variables or expressions into strings. The `format()` method uses placeholders `{}` to insert values, while f-strings (introduced in Python 3.6) allow direct variable embedding with `f` prefix.

### Examples:
- Using `format()`:
  ```python
  name = "Alice"
  text = "Hello, {}".format(name)
  print(text)  # Output: Hello, Alice
  ```

- Using f-strings:
  ```python
  name = "Bob"
  text = f"Hello, {name}"
  print(text)  # Output: Hello, Bob
  ```

## Q2: Explain slicing in strings with examples, and write a program to reverse a string and check if it is a palindrome.
Slicing extracts parts of a string using `[start:stop:step]`. A palindrome is a string that reads the same forward and backward.

### Examples:
- Slicing:
  ```python
  text = "Python"
  print(text[1:4])  # Output: yth
  ```

### Program:
```python
text = "radar"
reversed_text = text[::-1]
print("Reversed string:", reversed_text)
is_palindrome = text == reversed_text
print("Is palindrome?", is_palindrome)  # Output: Reversed string: radar, Is palindrome? True
```

## Q3: What are escape sequences in strings? List and explain at least three common escape sequences in Python.
Escape sequences are special characters starting with `\` to represent non-printable characters.

### Common Escape Sequences:
- `\n`: Newline - Moves the cursor to the next line.
- `\t`: Tab - Inserts a horizontal tab space.
- `\"`: Double quote - Inserts a double quote without ending the string.

## Q4: Write a program to format a string to display a floating-point number with two decimal places.
```python
number = 3.14159
formatted = f"Number: {number:.2f}"
print(formatted)  # Output: Number: 3.14
```

## Q5: Define lists and tuples in Python. How are they created, and what are the key differences between them?
- **Lists**: Mutable, ordered collections created with `[]`.
  ```python
  my_list = [1, 2, 3]
  ```
- **Tuples**: Immutable, ordered collections created with `()`.
  ```python
  my_tuple = (1, 2, 3)
  ```
- **Key Differences**: Lists can be modified (add, remove, update), tuples cannot.

## Q6: How can you add, update, and remove elements in a list? Why can’t you perform the same operations on tuples?
- **List Operations**:
  ```python
  my_list = [1, 2, 3]
  my_list.append(4)    # Add
  my_list[1] = 5       # Update
  my_list.pop()        # Remove
  ```
- **Tuples**: Immutable, so no methods like `append` or `pop` are available.

## Q7: Write a program that demonstrates slicing and iteration for both lists and tuples.
```python
my_list = [1, 2, 3, 4]
my_tuple = (5, 6, 7, 8)

# Slicing
print(my_list[1:3])    # Output: [2, 3]
print(my_tuple[1:3])   # Output: (6, 7)

# Iteration
for item in my_list:
    print(item, end=" ")  # Output: 1 2 3 4
print()
for item in my_tuple:
    print(item, end=" ")  # Output: 5 6 7 8
```

## Q8: Explain unpacking in lists and tuples with examples.
Unpacking assigns elements to variables.

### Examples:
- List:
  ```python
  my_list = [1, 2, 3]
  a, b, c = my_list
  print(a, b, c)  # Output: 1 2 3
  ```
- Tuple:
  ```python
  my_tuple = (4, 5, 6)
  x, y, z = my_tuple
  print(x, y, z)  # Output: 4 5 6
  ```

## Q9: What is mutability in Python? Why are lists mutable and tuples immutable? Provide examples.
- **Mutability**: Ability to change an object after creation.
- **Lists**: Mutable (can change content).
  ```python
  my_list = [1, 2, 3]
  my_list[0] = 10
  print(my_list)  # Output: [10, 2, 3]
  ```
- **Tuples**: Immutable (cannot change content).
  ```python
  my_tuple = (1, 2, 3)
  # my_tuple[0] = 10  # This will raise an error
  ```
- **Reason**: Lists are designed for dynamic data, tuples for fixed data.

## Q10: Can you modify a tuple that contains mutable objects like lists? Explain with an example.
Yes, if a tuple contains mutable objects, you can modify those objects.

### Example:
```python
my_tuple = (1, [2, 3], 4)
my_tuple[1][0] = 5
print(my_tuple)  # Output: (1, [5, 3], 4)
```

## Q11: Write a program to demonstrate that changes in one variable affect another when referencing the same list.
```python
list1 = [1, 2, 3]
list2 = list1
list2[0] = 10
print("list1:", list1)  # Output: list1: [10, 2, 3]
print("list2:", list2)  # Output: list2: [10, 2, 3]
```

## Q12: Explain shallow copy and deep copy in detail with examples.
- **Shallow Copy**: Creates a new object but references nested objects.
  ```python
  import copy
  list1 = [[1, 2], 3]
  list2 = copy.copy(list1)
  list2[0][0] = 10
  print(list1)  # Output: [[10, 2], 3]
  ```
- **Deep Copy**: Creates a new object and recursively copies nested objects.
  ```python
  import copy
  list1 = [[1, 2], 3]
  list2 = copy.deepcopy(list1)
  list2[0][0] = 10
  print(list1)  # Output: [[1, 2], 3]
  ```