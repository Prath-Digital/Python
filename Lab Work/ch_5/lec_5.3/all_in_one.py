def q1_add_or_concat(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return str(a) + str(b)

def q2_shape_area(shape):
    if isinstance(shape, Circle):
        return 3.14 * shape.radius * shape.radius
    elif isinstance(shape, Rectangle):
        return shape.length * shape.width

class Circle:
    def __init__(self, radius):
        self.radius = radius

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

def q3_len_demo(obj):
    if isinstance(obj, str):
        return len(obj)
    elif isinstance(obj, list):
        return len(obj)
    elif isinstance(obj, dict):
        return len(obj)

class Transport:
    def travel(self):
        pass

class Train(Transport):
    def travel(self):
        return "Train is traveling on rails."

class Plane(Transport):
    def travel(self):
        return "Plane is flying in the sky."

class Calculator:
    def multiply(self, a, b=1, c=1):
        return a * b * c

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Shape:
    @staticmethod
    def area():
        pass

class CircleShape(Shape):
    @staticmethod
    def area(radius):
        return 3.14 * radius * radius

class RectangleShape(Shape):
    @staticmethod
    def area(length, width):
        return length * width

class Vehicle:
    def start(self):
        pass

class Bike(Vehicle):
    def start(self):
        return "Bike is starting with a kick!"

class Car(Vehicle):
    def start(self):
        return "Car is starting with a key!"

class Printer:
    def print(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            return args[0]
        elif len(args) == 1 and isinstance(args[0], int):
            return str(args[0])
        elif len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], int):
            return args[0] + str(args[1])

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    pass

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

class Grandparent:
    pass

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

class Base:
    def display(self):
        return "Base display"

class Derived(Base):
    def display(self):
        return super().display() + " -> Derived display"

class User:
    def __init__(self, name):
        self.name = name

class Admin(User):
    def __init__(self, name):
        super().__init__(name)

def main():
    while True:
        print("\nMenu:")
        print("1. Q1: Add/Concatenate")
        print("2. Q2: Shape Area")
        print("3. Q3: Len Demo")
        print("4. Q4: Transport Travel")
        print("5. Q5: Calculator Multiply")
        print("6. Q6: Animal Speak")
        print("7. Q7: Shape Area (Static)")
        print("8. Q8: Vehicle Start")
        print("9. Q9: Printer")
        print("10. Q10: Issubclass Demo")
        print("11. Q11: Manager Constructor")
        print("12. Q12: Multilevel Inheritance")
        print("13. Q13: Super in Method")
        print("14. Q14: Admin Constructor")
        print("0. Exit")
        
        choice = int(input("Enter your choice (0-14): "))
        
        if choice == 1:
            a = input("Enter first value: ")
            b = input("Enter second value: ")
            try:
                a = int(a)
                b = int(b)
            except ValueError:
                pass
            print("Result:", q1_add_or_concat(a, b))
        
        elif choice == 2:
            shape_type = input("Enter shape (Circle/Rectangle): ")
            if shape_type.lower() == "circle":
                radius = float(input("Enter radius: "))
                print("Area:", q2_shape_area(Circle(radius)))
            elif shape_type.lower() == "rectangle":
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                print("Area:", q2_shape_area(Rectangle(length, width)))
        
        elif choice == 3:
            obj_type = input("Enter type (str/list/dict): ")
            if obj_type.lower() == "str":
                obj = input("Enter string: ")
                print("Length:", q3_len_demo(obj))
            elif obj_type.lower() == "list":
                obj = input("Enter list elements separated by space: ").split()
                print("Length:", q3_len_demo(obj))
            elif obj_type.lower() == "dict":
                obj = eval(input("Enter dictionary (e.g., {'a': 1}): "))
                print("Length:", q3_len_demo(obj))
        
        elif choice == 4:
            transport = Train() if input("Enter Transport (Train/Plane): ").lower() == "train" else Plane()
            print("Travel:", transport.travel())
        
        elif choice == 5:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number (default 1): ") or 1)
            c = float(input("Enter third number (default 1): ") or 1)
            calc = Calculator()
            print("Result:", calc.multiply(a, b, c))
        
        elif choice == 6:
            animal = Dog() if input("Enter Animal (Dog/Cat): ").lower() == "dog" else Cat()
            print("Sound:", animal.speak())
        
        elif choice == 7:
            shape_type = input("Enter shape (Circle/Rectangle): ")
            if shape_type.lower() == "circle":
                radius = float(input("Enter radius: "))
                print("Area:", CircleShape.area(radius))
            elif shape_type.lower() == "rectangle":
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                print("Area:", RectangleShape.area(length, width))
        
        elif choice == 8:
            vehicle = Bike() if input("Enter Vehicle (Bike/Car): ").lower() == "bike" else Car()
            print("Start:", vehicle.start())
        
        elif choice == 9:
            args = input("Enter string or integer or both (space-separated): ").split()
            printer = Printer()
            print("Printed:", printer.print(*args))
        
        elif choice == 10:
            print("Is Student a subclass of Person?", issubclass(Student, Person))
        
        elif choice == 11:
            name = input("Enter Manager name: ")
            salary = float(input("Enter salary: "))
            manager = Manager(name, salary)
            print(f"Manager: {manager.name}, Salary: {manager.salary}")
        
        elif choice == 12:
            child = Child()
            print("Is Child a subclass of Parent?", issubclass(Child, Parent))
            print("Is Child a subclass of Grandparent?", issubclass(Child, Grandparent))
        
        elif choice == 13:
            derived = Derived()
            print("Display:", derived.display())
        
        elif choice == 14:
            name = input("Enter Admin name: ")
            admin = Admin(name)
            print(f"Admin: {admin.name}")
        
        elif choice == 0:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()