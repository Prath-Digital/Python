# Python Dunder Methods Questions and Answers

## Q1: What are dunder (double underscore) methods in Python, and why are they used?
Dunder methods, or magic methods, are special methods in Python with double underscores (e.g., `__init__`, `__str__`). They allow customization of a class's behavior for built-in operations like initialization, string representation, and operator overloading. They are used to make classes more intuitive and Pythonic by defining how objects interact with language constructs.

## Q2: Explain the purpose of the `__init__` method with an example.
The `__init__` method is a constructor that initializes a new instance of a class. It is called automatically when a new object is created.
```python
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Alice")
print(person.name)  # Output: Alice
```

## Q3: What is the role of the `__str__` and `__repr__` methods in Python? How do they differ?
- `__str__` returns a human-readable string representation of an object, mainly for end users.
- `__repr__` returns a detailed string representation, ideally to recreate the object, mainly for developers.
```python
class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Name: {self.name}"
    def __repr__(self):
        return f"Person(name='{self.name}')"

person = Person("Alice")
print(str(person))  # Output: Name: Alice
print(repr(person))  # Output: Person(name='Alice')
```
- `__str__` is for readability, while `__repr__` is for unambiguous representation.

## Q4: Describe the purpose of the `__len__` and `__getitem__` methods. Provide examples.
- `__len__` returns the length of an object, used with the `len()` function.
- `__getitem__` allows indexing or slicing, used with `obj[key]`.
```python
class MyList:
    def __init__(self, data):
        self.data = data
    def __len__(self):
        return len(self.data)
    def __getitem__(self, index):
        return self.data[index]

my_list = MyList([1, 2, 3])
print(len(my_list))      # Output: 3
print(my_list[1])        # Output: 2
```

## Q5: What is the significance of the `__call__` method in Python? Demonstrate its usage with an example.
The `__call__` method allows an object to be called like a function. It enables instances to behave as callable objects.
```python
class Adder:
    def __init__(self, value):
        self.value = value
    def __call__(self, x):
        return self.value + x

add_five = Adder(5)
print(add_five(3))  # Output: 8
```

## Q6: How do the `__eq__` and `__lt__` methods work for comparison in Python? Provide an example program.
- `__eq__` defines equality (`==`) comparison.
- `__lt__` defines less than (`<`) comparison.
```python
class Number:
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        if isinstance(other, Number):
            return self.value == other.value
        return False
    def __lt__(self, other):
        if isinstance(other, Number):
            return self.value < other.value
        return NotImplemented

num1 = Number(5)
num2 = Number(3)
print(num1 == num2)  # Output: False
print(num1 < num2)   # Output: False
```

## Q7: What is operator overloading in Python, and why is it useful?
Operator overloading allows custom objects to use Python operators (e.g., `+`, `*`) by defining special methods. It is useful for making custom classes intuitive and consistent with built-in types.

## Q8: Explain how the `+` operator can be overloaded for custom objects using the `__add__` method. Provide an example.
The `__add__` method overloads the `+` operator.
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
print(v1 + v2)  # Output: (6, 8)
```

## Q9: Write a program to demonstrate overloading the `*` operator using the `__mul__` method.
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented
    def __str__(self):
        return f"({self.x}, {self.y})"

v = Vector(2, 3)
print(v * 2)  # Output: (4, 6)
```

## Q10: What are the limitations of operator overloading in Python?
Operator overloading is limited to specific methods (e.g., `__add__`, `__mul__`) and cannot be applied to all operators or custom syntax. It requires careful implementation to avoid ambiguity and must return `NotImplemented` for incompatible types.

## Q11: Can relational operators like `>` or `<` be overloaded? Demonstrate with an example.
Yes, relational operators can be overloaded using methods like `__gt__` (>) or `__lt__` (<).
```python
class Number:
    def __init__(self, value):
        self.value = value
    def __gt__(self, other):
        if isinstance(other, Number):
            return self.value > other.value
        return NotImplemented

num1 = Number(5)
num2 = Number(3)
print(num1 > num2)  # Output: True
```

## Q12: Write a Python program to overload the `==` operator to compare two objects based on a specific attribute.
```python
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.id == other.id
        return False
    def __str__(self):
        return f"Student(id={self.id}, name={self.name})"

s1 = Student(1, "Alice")
s2 = Student(1, "Bob")
print(s1 == s2)  # Output: True
```