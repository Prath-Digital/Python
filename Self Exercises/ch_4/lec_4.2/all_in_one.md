# Python Programming Concepts - Questions and Answers

## Q1: What is recursion in Python, and how is it different from iteration?
Recursion in Python is a process where a function calls itself to solve a problem. It differs from iteration, which uses loops to repeat a set of instructions. Recursion breaks problems into smaller subproblems, while iteration repeats a block of code.

## Q2: Explain the significance of the base condition in recursive functions. Provide an example.
The base condition in recursive functions is crucial as it stops the recursion to prevent infinite loops. Without it, the function would call itself indefinitely.  
**Example:**  
```python
def factorial(n):
    if n == 0 or n == 1:  # Base condition
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120
```

## Q3: Write a recursive function to calculate the Fibonacci series up to a given number.
```python
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2] if len(fib_series) > 1 else 1)
        return fib_series

print(fibonacci(7))  # Output: [0, 1, 1, 2, 3, 5, 8]
```

## Q4: What are the potential drawbacks of using recursion, and how can they be mitigated?
Drawbacks include stack overflow for deep recursion due to limited stack space and performance overhead from multiple function calls. Mitigation includes using iteration instead or optimizing with tail recursion where supported.

## Q5: What are anonymous functions (lambda functions) in Python, and how do they differ from regular functions?
Lambda functions are small, anonymous functions defined with the `lambda` keyword, used for short, simple operations. They differ from regular functions (defined with `def`) as they are limited to a single expression and lack a name.

## Q6: Write a Python program to demonstrate the use of a lambda function to calculate the square of a number.
```python
square = lambda x: x * x
print(square(5))  # Output: 25
```

## Q7: Discuss the use of lambda functions in combination with functions like map(), filter(), and reduce(). Provide examples.
Lambda functions are often used with `map()` to apply a function to all items, `filter()` to select items, and `reduce()` to accumulate results.  
**Examples:**  
```python
from functools import reduce
numbers = [1, 2, 3, 4]
squares = map(lambda x: x**2, numbers)  # [1, 4, 9, 16]
filtered = filter(lambda x: x > 2, numbers)  # [3, 4]
sum_val = reduce(lambda x, y: x + y, numbers)  # 10
```

## Q8: What are the limitations of lambda functions in Python?
Lambda functions are limited to a single expression, cannot contain statements (e.g., `if`, `for`), and are less readable for complex logic compared to regular functions.

## Q9: What is the purpose of the global keyword in Python? When should it be used?
The `global` keyword allows a function to modify a variable outside its scope, declared in the global namespace. It should be used sparingly, only when a variable needs to be modified globally, to avoid unintended side effects.

## Q10: Write a Python program that uses the global keyword to modify a variable outside the function scope.
```python
x = 10
def modify_global():
    global x
    x = 20
modify_global()
print(x)  # Output: 20
```

## Q11: What is the difference between using the global keyword and returning values from a function?
Using `global` modifies a variable in the global scope directly, affecting all parts of the program. Returning values allows a function to pass data back to the caller without altering the global state, promoting encapsulation.

## Q12: How can a Python function return multiple values? Write a program to demonstrate returning multiple values from a function using a list and a dictionary.
```python
# Using a list
def return_list():
    return [1, 2, 3]
result_list = return_list()
print(result_list)  # Output: [1, 2, 3]

# Using a dictionary
def return_dict():
    return {"a": 1, "b": 2}
result_dict = return_dict()
print(result_dict)  # Output: {'a': 1, 'b': 2}
```