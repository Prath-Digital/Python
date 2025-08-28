# Python Control Statements and List Comprehension Q&A

## Q.1 What are control statements in Python, and why are they used? List the three main control statements in Python and briefly explain each.

**Answer**:  
Control statements in Python are used to control the flow of a program’s execution based on certain conditions or iterations. They allow the program to make decisions, repeat actions, or skip certain parts of code, enabling dynamic and flexible program behavior.

The three main control statements in Python are:

1. **Conditional Statements (if, elif, else)**: These allow the program to execute specific blocks of code based on whether a condition is true or false. For example, `if` checks a condition, `elif` checks additional conditions if the previous ones are false, and `else` handles the default case when no conditions are met.
2. **Looping Statements (for, while)**: These enable the program to repeat a block of code multiple times. A `for` loop iterates over a sequence (like a list or range), while a `while` loop continues executing as long as a condition remains true.
3. **Control Flow Tools (break, continue, pass)**: These modify the behavior of loops or conditionals. `break` exits a loop prematurely, `continue` skips the current iteration and moves to the next, and `pass` is a placeholder that does nothing, often used to maintain syntactic structure.

---

## Q.2 How does the else clause work with loops in Python? Provide an example.

**Answer**:  
The `else` clause in Python loops executes when the loop completes normally (i.e., without being terminated by a `break` statement). It is typically used to handle cases where the loop finishes its iteration without encountering a specific condition that would cause an early exit.

**Example**:  
```python
for i in range(5):
    if i == 6:
        print("Found 6, breaking loop")
        break
    print(f"Iteration: {i}")
else:
    print("Loop completed without finding 6")
```

**Output**:  
```
Iteration: 0
Iteration: 1
Iteration: 2
Iteration: 3
Iteration: 4
Loop completed without finding 6
```

---

## Q.3 Write a program that uses the break statement to exit a loop when a specific condition is met.

**Answer**:  
```python
for num in range(1, 10):
    if num == 5:
        print(f"Found {num}, exiting loop")
        break
    print(f"Current number: {num}")
```

**Output**:  
```
Current number: 1
Current number: 2
Current number: 3
Current number: 4
Found 5, exiting loop
```

---

## Q.4 What is the difference between break, continue, and pass statements?

**Answer**:  
- **break**: Terminates the entire loop immediately and transfers control to the code after the loop. It is used to exit a loop when a specific condition is met.
- **continue**: Skips the rest of the current iteration and moves to the next iteration of the loop. It does not terminate the loop but skips the remaining code in the current cycle.
- **pass**: A null operation that does nothing when executed. It is used as a placeholder in code where a statement is syntactically required but no action is needed.

**Example**:  
```python
for i in range(1, 6):
    if i == 2:
        continue  # Skip iteration when i is 2
    if i == 4:
        break    # Exit loop when i is 4
    if i == 3:
        pass     # Do nothing when i is 3
    print(i)
```

**Output**:  
```
1
3
```

---

## Q.5 What is list comprehension in Python, and why is it preferred over traditional loops?

**Answer**:  
List comprehension is a concise way to create lists in Python using a single line of code. It combines a loop and optional condition(s) to generate a list based on an iterable.

**Why Preferred**:  
- **Conciseness**: Reduces multiple lines of code into a single, readable line.
- **Clarity**: Makes code more compact and often easier to understand for simple transformations or filtering.
- **Performance**: Slightly faster than traditional loops due to optimized implementation in Python.

However, for complex logic, traditional loops may be more readable.

---

## Q.6 Explain the syntax of list comprehension with an example.

**Answer**:  
**Syntax**:  
```python
[expression for item in iterable if condition]
```
- **expression**: The operation to perform on each `item`.
- **item**: The variable representing each element in the `iterable`.
- **iterable**: A sequence (e.g., list, range, string) to iterate over.
- **if condition** (optional): Filters items based on a condition.

**Example**:  
```python
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers if x % 2 == 0]
print(squares)
```

**Output**:  
```
[4, 16]
```

---

## Q.7 How does list comprehension differ from using a for loop to create a list?

**Answer**:  
- **List Comprehension**:  
  - Single line, concise syntax.
  - Directly creates a new list.
  - Less verbose, but can be less readable for complex logic.
  - Example: `squares = [x**2 for x in range(1, 6)]`

- **For Loop**:  
  - Multiple lines, more explicit.
  - Requires manually appending to a list.
  - More flexible for complex operations or when readability is prioritized.
  - Example:  
    ```python
    squares = []
    for x in range(1, 6):
        squares.append(x**2)
    ```

Both produce the same result (`[1, 4, 9, 16, 25]`), but list comprehension is more concise.

---

## Q.8 Write a list comprehension to generate a list of squares of numbers from 1 to 10.

**Answer**:  
```python
squares = [x**2 for x in range(1, 11)]
print(squares)
```

**Output**:  
```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

---

## Q.9 Write a list comprehension to create a list of even numbers from 1 to 20.

**Answer**:  
```python
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)
```

**Output**:  
```
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

---

## Q.10 Can list comprehension be nested? Provide an example to demonstrate this.

**Answer**:  
Yes, list comprehensions can be nested, allowing the creation of lists within lists (e.g., for matrix-like structures) by including one list comprehension inside another.

**Example**:  
```python
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)
```

**Output**:  
```
[[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

---

## Q.11 Write a program to filter out vowels from a given string using list comprehension.

**Answer**:  
```python
text = "Hello World"
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
filtered = [char for char in text if char not in vowels]
print(''.join(filtered))
```

**Output**:  
```
Hll Wrld
```

---

## Q.12 What is a nested loop in Python, and how is it structured?

**Answer**:  
A nested loop in Python is a loop inside another loop. The inner loop runs completely for each iteration of the outer loop, often used for working with multi-dimensional data like matrices or generating combinations.

**Structure**:  
```python
for outer_variable in outer_iterable:
    # Outer loop code
    for inner_variable in inner_iterable:
        # Inner loop code
```

**Example**:  
```python
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i={i}, j={j}, product={i*j}")
```

**Output**:  
```
i=1, j=1, product=1
i=1, j=2, product=2
i=2, j=1, product=2
i=2, j=2, product=4
i=3, j=1, product=3
i=3, j=2, product=6
```