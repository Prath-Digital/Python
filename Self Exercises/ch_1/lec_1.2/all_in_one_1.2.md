# Python Basics – Questions and Answers

## Q1. Explain the use of the `sep` and `end` parameters in the `print()` function. Provide examples.

**_Answer:_**  
The `print()` function in Python has two optional parameters: `sep` and `end`.

- `sep`: Specifies the separator between multiple arguments. The default is a space (" ").
- `end`: Specifies what to print at the end of the output. The default is a newline ("\n").

```python
print("Hello", "World", sep="-")
print("Hello", end=" ")
print("World")
```

---

## Q2. What is the difference between printing a string with single quotes, double quotes, and triple quotes in Python?

**_Answer:_**  
In Python, strings can be defined using single quotes ('), double quotes ("), or triple quotes (''' or """).

- Single quotes and double quotes are interchangeable for simple strings.
- Triple quotes are used for multi-line strings or strings containing single/double quotes without escaping.

```python
print('Hello')
print("World")
print("""This is a
multi-line string""")
```

---

## Q3. Explain the default data type the `input()` function returns. How can you convert it to another type?

**_Answer:_**  
The `input()` function returns a string by default. To convert it to another type, use type-casting functions like `int()`, `float()`, or others.

```python
user_input = input("Enter a number: ")
number = int(user_input)
print(number + 5)
```

---

## Q4. Write a Python program that takes two numbers as input, adds them, and displays the result using `print()`.

**_Answer:_**

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_result = num1 + num2
print
```
