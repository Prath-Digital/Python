class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

class Sentence:
    def __init__(self, text):
        self.text = text
    
    def __len__(self):
        return len(self.text.split())

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        return False

class Box:
    def __init__(self, items):
        self.items = items
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def __repr__(self):
        return f"BankAccount(name={self.name}, balance={self.balance})"

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            real_part = self.real * other.real - self.imaginary * other.imaginary
            imag_part = self.real * other.imaginary + self.imaginary * other.real
            return ComplexNumber(real_part, imag_part)
        return NotImplemented
    
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    def __gt__(self, other):
        if isinstance(other, Time):
            if self.hours > other.hours:
                return True
            elif self.hours == other.hours and self.minutes > other.minutes:
                return True
            return False
        return NotImplemented

class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    
    def __sub__(self, discount):
        if isinstance(discount, (int, float)):
            return Book(self.title, self.price - discount)
        return NotImplemented
    
    def __str__(self):
        return f"Book(title={self.title}, price={self.price})"

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def __getitem__(self, row):
        return self.matrix[row]

# Menu-driven program
while True:
    print("\nMenu:")
    print("1. Point - String representation")
    print("2. Sentence - Word count")
    print("3. Rectangle - Compare areas")
    print("4. Box - Access/Modify items")
    print("5. BankAccount - Developer representation")
    print("6. Vector - Addition")
    print("7. ComplexNumber - Multiplication")
    print("8. Time - Compare")
    print("9. Book - Apply discount")
    print("10. Matrix - Access row")
    print("0. Exit")
    
    choice = int(input("Enter your choice (0-10): "))
    
    if choice == 1:
        x = int(input("Enter x coordinate: "))
        y = int(input("Enter y coordinate: "))
        p = Point(x, y)
        print("Point:", p)
    
    elif choice == 2:
        text = input("Enter a sentence: ")
        s = Sentence(text)
        print("Number of words:", len(s))
    
    elif choice == 3:
        l1 = int(input("Enter length of first rectangle: "))
        b1 = int(input("Enter breadth of first rectangle: "))
        l2 = int(input("Enter length of second rectangle: "))
        b2 = int(input("Enter breadth of second rectangle: "))
        r1 = Rectangle(l1, b1)
        r2 = Rectangle(l2, b2)
        print("Are areas equal?", r1 == r2)
    
    elif choice == 4:
        items = [int(x) for x in input("Enter items separated by space: ").split()]
        b = Box(items)
        index = int(input("Enter index to access: "))
        print("Item at index:", b[index])
        new_value = int(input("Enter new value to set: "))
        b[index] = new_value
        print("Updated items:", b.items)
    
    elif choice == 5:
        name = input("Enter account holder name: ")
        balance = float(input("Enter balance: "))
        acc = BankAccount(name, balance)
        print("Account:", acc)
    
    elif choice == 6:
        x1 = int(input("Enter x1: "))
        y1 = int(input("Enter y1: "))
        x2 = int(input("Enter x2: "))
        y2 = int(input("Enter y2: "))
        v1 = Vector(x1, y1)
        v2 = Vector(x2, y2)
        v3 = v1 + v2
        print("Resultant Vector:", (v3.x, v3.y))
    
    elif choice == 7:
        r1 = int(input("Enter real part of first number: "))
        i1 = int(input("Enter imaginary part of first number: "))
        r2 = int(input("Enter real part of second number: "))
        i2 = int(input("Enter imaginary part of second number: "))
        c1 = ComplexNumber(r1, i1)
        c2 = ComplexNumber(r2, i2)
        c3 = c1 * c2
        print("Result:", c3)
    
    elif choice == 8:
        h1 = int(input("Enter hours for first time: "))
        m1 = int(input("Enter minutes for first time: "))
        h2 = int(input("Enter hours for second time: "))
        m2 = int(input("Enter minutes for second time: "))
        t1 = Time(h1, m1)
        t2 = Time(h2, m2)
        print("Is first time greater?", t1 > t2)
    
    elif choice == 9:
        title = input("Enter book title: ")
        price = float(input("Enter book price: "))
        discount = float(input("Enter discount amount: "))
        b = Book(title, price)
        b_discounted = b - discount
        print("Discounted Book:", b_discounted)
    
    elif choice == 10:
        rows = int(input("Enter number of rows: "))
        matrix = []
        for i in range(rows):
            row = [int(x) for x in input(f"Enter row {i+1} elements: ").split()]
            matrix.append(row)
        m = Matrix(matrix)
        row = int(input("Enter row index to access: "))
        print("Row:", m[row])
    
    elif choice == 0:
        print("Exiting...")
        break
    
    else:
        print("Invalid choice! Please try again.")