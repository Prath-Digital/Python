# Single Inheritance
class Parent:
    def display(self):
        print("This is Parent's display method")


class Child(Parent):
    pass


# Multiple Inheritance
class Teacher:
    def teach(self):
        print("Teaching students")


class Administrator:
    def manage(self):
        print("Managing school")


class Headmaster(Teacher, Administrator):
    pass


# Multilevel Inheritance
class Grandparent:
    def role(self):
        print("I am Grandparent")


class Parent1(Grandparent):
    def role(self):
        print("I am Parent")


class Child1(Parent1):
    def role(self):
        print("I am Child")


# Hierarchical Inheritance
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Barking")


class Cat(Animal):
    def meow(self):
        print("Meowing")


# Hybrid Inheritance
class A:
    def method_a(self):
        print("Method A")


class B(A):
    def method_b(self):
        print("Method B")


class C(A):
    def method_c(self):
        print("Method C")


class D(B, C):
    def method_d(self):
        print("Method D from D")

    def resolve_ambiguity(self):
        super().method_b()  # Resolving ambiguity by explicit call


# Type, id, dir, isinstance, help examples
def type_demo():
    x = 10
    y = "hello"
    print(f"Type of x: {type(x)}")
    print(f"Type of y: {type(y)}")


def id_demo():
    a = 5
    b = 5
    print(f"Memory location of a: {id(a)}")
    print(f"Memory location of b: {id(b)}")


def dir_demo():
    class Sample:
        def __init__(self):
            self.name = "Test"

        def show(self):
            print("Show method")

    obj = Sample()
    print(dir(obj))


def isinstance_demo():
    class TestClass:
        pass

    obj = TestClass()
    print(f"Is obj an instance of TestClass? {isinstance(obj, TestClass)}")


def help_demo():
    def sample_func():
        """This is a sample function."""
        pass

    help(sample_func)


# Nested Functions
def outer_square_cube(num):
    def inner_cube():
        return num**3

    square = num**2
    cube = inner_cube()
    print(f"Square: {square}, Cube: {cube}")


def outer_string_length(input_str):
    def inner_length():
        return len(input_str)

    length = inner_length()
    print(f"Length of string: {length}")


def outer_rect_square(length, width):
    def inner_square():
        return length * length

    area_rect = length * width
    area_square = inner_square()
    print(f"Rectangle Area: {area_rect}, Square Area: {area_square}")


# Menu Driven Program
while True:
    print("\nMenu:")
    print("1. Single Inheritance")
    print("2. Multiple Inheritance")
    print("3. Multilevel Inheritance")
    print("4. Hierarchical Inheritance")
    print("5. Hybrid Inheritance")
    print("6. Type Function Demo")
    print("7. ID Function Demo")
    print("8. Dir Function Demo")
    print("9. Isinstance Function Demo")
    print("10. Help Function Demo")
    print("11. Square and Cube (Nested)")
    print("12. String Length (Nested)")
    print("13. Rectangle and Square Area (Nested)")
    print("0. Exit")

    choice = int(input("Enter your choice (0-13): "))

    if choice == 1:
        c = Child()
        c.display()
    elif choice == 2:
        h = Headmaster()
        h.teach()
        h.manage()
    elif choice == 3:
        c1 = Child1()
        c1.role()
    elif choice == 4:
        d = Dog()
        c = Cat()
        d.eat()
        d.bark()
        c.eat()
        c.meow()
    elif choice == 5:
        d = D()
        d.method_d()
        d.resolve_ambiguity()
    elif choice == 6:
        type_demo()
    elif choice == 7:
        id_demo()
    elif choice == 8:
        dir_demo()
    elif choice == 9:
        isinstance_demo()
    elif choice == 10:
        help_demo()
    elif choice == 11:
        num = int(input("Enter a number: "))
        outer_square_cube(num)
    elif choice == 12:
        stri = input("Enter a string: ")
        outer_string_length(stri)
    elif choice == 13:
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        outer_rect_square(l, w)
    elif choice == 0:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")
