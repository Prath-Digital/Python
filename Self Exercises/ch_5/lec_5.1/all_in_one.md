# OOP in Python - Questions and Answers

## Q1. What are the four principles of Object-Oriented Programming (OOP)? Explain each with examples.

- **Encapsulation**: Bundling data and methods that operate on the data within a single unit (class). Example: A `Car` class with private attributes like `_speed` accessed via methods.
- **Abstraction**: Hiding complex implementation details and showing only the necessary features. Example: A `Calculator` class with a `add()` method without exposing the internal logic.
- **Inheritance**: Allowing a class to inherit attributes and methods from another class. Example: A `SportsCar` class inheriting from a `Car` class.
- **Polymorphism**: Allowing methods to be used in different ways. Example: A `display()` method behaving differently in `Car` and `Truck` classes.

## Q2. How do the principles of OOP help in building reusable and modular code?

The principles promote reusability by allowing code reuse through inheritance and modularity by encapsulating functionality into classes, making it easier to maintain and extend.

## Q3. What is a class in Python, and how does it differ from an object? Provide examples.

- A **class** is a blueprint for creating objects (e.g., `class Car:` defines attributes and methods).
- An **object** is an instance of a class (e.g., `my_car = Car()`). Example: `class Dog:` (class) vs. `my_dog = Dog()` (object).

## Q4. Write a Python program to create a class Car with attributes brand and model and a method display_info(). Create an object to call the method.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

my_car = Car("Toyota", "Camry")
my_car.display_info()  # Output: Brand: Toyota, Model: Camry
```

## Q5. What is the purpose of the self keyword in Python classes? Why is it required in instance methods?

The `self` keyword represents the instance of the class, allowing access to its attributes and methods. It's required in instance methods to differentiate instance-specific data from class-level data.

## Q6. Explain the role of the del keyword in Python. How is it used to delete objects or attributes? Provide examples.

The `del` keyword deletes objects or attributes. Example: 
- Deleting an attribute: `del obj.attr`
- Deleting an object: `del obj` (removes the reference, and garbage collection may free memory).

## Q7. What is a constructor in Python? How is it implemented using the __init__ method?

A constructor initializes a new object. It's implemented using the `__init__` method, which runs automatically when an object is created. Example: `def __init__(self, name): self.name = name`.

## Q8. Explain the types of constructors in Python with examples (default and parameterized).

- **Default Constructor**: No parameters, uses default values. Example: `def __init__(self): self.value = 0`
- **Parameterized Constructor**: Takes parameters. Example: `def __init__(self, value): self.value = value`

## Q9. What is a destructor in Python? How is it implemented using the __del__ method? Provide an example.

A destructor cleans up when an object is deleted. It's implemented with `__del__`, called before garbage collection. Example:
```python
class Test:
    def __del__(self):
        print("Object deleted")
obj = Test()  # Output: Object deleted (when obj is deleted)
```

## Q10. What is encapsulation in Python, and how does it promote data security?

Encapsulation bundles data and methods, restricting direct access to some attributes (e.g., using private variables). It promotes data security by preventing unintended modifications.

## Q11. Explain how private attributes are declared and accessed using public methods in Python. Provide an example.

Private attributes use a double underscore (e.g., `__attr`). They’re accessed via public methods. Example:
```python
class Person:
    def __init__(self):
        self.__name = "John"
    
    def get_name(self):
        return self.__name

person = Person()
print(person.get_name())  # Output: John
```

## Q12. Write a program to demonstrate encapsulation by creating a class with private attributes and public getter and setter methods.

```python
class BankAccount:
    def __init__(self):
        self.__balance = 0
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
    
    account = BankAccount()
    account.set_balance(1000)
    print(account.get_balance())  # Output: 1000
```