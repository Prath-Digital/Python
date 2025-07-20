# Python Programming Questions and Answers

## Q1: What is inheritance in Python, and why is it important in Object-Oriented Programming?
**Answer:** Inheritance in Python is a way for one class to inherit properties and methods from another class. It’s super important in Object-Oriented Programming because it promotes code reuse, makes maintenance easier, and supports the concept of hierarchy. For example, a `Dog` class can inherit from a `Animal` class.

## Q2: Explain the different types of inheritance supported in Python with examples (Single, Multiple, Multilevel, Hierarchical, and Hybrid).
**Answer:** 
- **Single:** One class inherits from one parent. Example: `class Dog(Animal):`.
- **Multiple:** One class inherits from multiple parents. Example: `class Baby(Dog, Cat):`.
- **Multilevel:** A chain of inheritance. Example: `class Puppy(Dog):` where `Dog` inherits from `Animal`.
- **Hierarchical:** Multiple classes inherit from one parent. Example: `class Dog(Animal):` and `class Cat(Animal):`.
- **Hybrid:** A mix of types, like multiple and multilevel. Example: Combine `Baby(Dog, Cat)` with further inheritance.

## Q3: Write a Python program to demonstrate multilevel inheritance with three classes.
**Answer:**
```python
class Animal:
    def eat(self):
        return "This animal eats food."

class Dog(Animal):
    def bark(self):
        return "The dog barks!"

class Puppy(Dog):
    def play(self):
        return "The puppy plays!"

pup = Puppy()
print(pup.eat())  # Output: This animal eats food.
print(pup.bark()) # Output: The dog barks!
print(pup.play()) # Output: The puppy plays!
```

## Q4: What is the difference between single and multiple inheritance? Provide examples.
**Answer:** Single inheritance involves one class inheriting from one parent, like `class Dog(Animal):`. Multiple inheritance involves one class inheriting from multiple parents, like `class Baby(Dog, Cat):`. The key difference is the number of parent classes—single has one, multiple has more!

## Q5: What is reflection in Python, and how does it help in understanding the structure of objects?
**Answer:** Reflection in Python is the ability of a program to inspect and modify its own structure and behavior at runtime. It helps understand object structure by letting you check attributes and methods dynamically, making code more flexible.

## Q6: Explain the use of the type() function in Python with examples.
**Answer:** The `type()` function returns the type of an object. Example: `print(type(5))` outputs `<class 'int'>`, and `print(type("hello"))` outputs `<class 'str'>`. It’s great for debugging or checking data types!

## Q7: How does the dir() function help in reflection? Write a Python program to list all attributes and methods of an object.
**Answer:**
```python
class Person:
    name = "Alice"
    def say_hello(self):
        return "Hello!"

p = Person()
print(dir(p))  # Output: Lists all attributes and methods like ['name', 'say_hello', ...]
```
The `dir()` function helps in reflection by showing all available attributes and methods of an object.

## Q8: Describe the purpose of the getattr(), setattr(), and hasattr() functions. Provide examples of each.
**Answer:** 
- **getattr():** Gets an attribute value. Example: `print(getattr(p, 'name'))` outputs `"Alice"`.
- **setattr():** Sets an attribute value. Example: `setattr(p, 'age', 25); print(p.age)` outputs `25`.
- **hasattr():** Checks if an attribute exists. Example: `print(hasattr(p, 'name'))` outputs `True`.
These functions help dynamically manage object properties.

## Q9: What is a nested function in Python, and how is it defined?
**Answer:** A nested function is a function defined inside another function. It’s defined by placing one `def` statement inside another. It’s useful for encapsulation and data privacy.

## Q10: Write a program to demonstrate the use of a nested function for calculating the area of a rectangle.
**Answer:**
```python
def calculate_area(length):
    def area_rect(width):
        return length * width
    return area_rect

area_calc = calculate_area(5)
print(area_calc(3))  # Output: 15
```

## Q11: What is the scope of variables in a nested function? Explain with an example.
**Answer:** Variables in a nested function have access to the outer function’s scope (enclosing scope) and their own local scope. Example:
```python
def outer():
    x = 10
    def inner():
        y = 5
        return x + y
    return inner()

print(outer())  # Output: 15 (accesses x from outer scope)
```

## Q12: How are nested functions used to implement closures in Python? Write a program to demonstrate this concept.
**Answer:** Nested functions create closures by remembering the enclosing scope even after the outer function finishes. Example:
```python
def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
print(add_five(3))  # Output: 8 (remembers x=5)
```