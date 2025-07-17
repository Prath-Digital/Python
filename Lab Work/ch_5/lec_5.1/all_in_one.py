class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
    
    def display_value(self):
        print(f"Count: {self.count}")

class Animal:
    def __init__(self, name):
        self.name = name
    
    def display_name(self):
        print(f"Animal Name: {self.name}")

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width

class Employee:
    def __init__(self):
        self.name = "Default"
    
    def __del__(self):
        print(f"Goodbye {self.name}! Object is being deleted.")

class Book:
    def __init__(self):
        self.__title = ""
        self.__author = ""
    
    def set_title(self, title):
        self.__title = title
    
    def set_author(self, author):
        self.__author = author
    
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author

class Account:
    def __init__(self):
        self.__balance = 0
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid amount!")
    
    def get_balance(self):
        return self.__balance

class PersonAge:
    def __init__(self):
        self.__age = 0
    
    def set_age(self, age):
        if age > 0:
            self.__age = age
            print(f"Age set to: {self.__age}")
        else:
            print("Age must be greater than 0!")
    
    def get_age(self):
        return self.__age

class Student:
    def __init__(self):
        self.__name = ""
        self.__marks = [0, 0, 0]
    
    def set_name(self, name):
        self.__name = name
    
    def set_marks(self, mark1, mark2, mark3):
        self.__marks = [mark1, mark2, mark3]
    
    def calculate_average(self):
        avg = sum(self.__marks) / 3
        print(f"Average marks for {self.__name}: {avg}")
        return avg
    
    def display_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        else:
            grade = "D"
        print(f"Grade for {self.__name}: {grade}")

def main():
    while True:
        print("\nMenu:")
        print("1. Person Details")
        print("2. Counter")
        print("3. Delete Objects")
        print("4. Animal Name")
        print("5. Rectangle Area")
        print("6. Employee Destructor")
        print("7. Book Attributes")
        print("8. Account Deposit")
        print("9. Age Validation")
        print("10. Student Average & Grade")
        print("11. Exit")
        
        choice = int(input("Enter your choice (1-11): "))
        
        if choice == 1:
            p1 = Person("Alice", 25)
            p2 = Person("Bob", 30)
            p1.display_details()
            p2.display_details()
        
        elif choice == 2:
            c1 = Counter()
            c1.increment()
            c1.display_value()
        
        elif choice == 3:
            obj1 = Counter()
            obj2 = Counter()
            del obj1
            del obj2
            print("Objects deleted. Check behavior!")
        
        elif choice == 4:
            a1 = Animal("Lion")
            a1.display_name()
        
        elif choice == 5:
            r1 = Rectangle(5, 3)
            print(f"Area of Rectangle: {r1.calculate_area()}")
        
        elif choice == 6:
            e1 = Employee()
            del e1
        
        elif choice == 7:
            b1 = Book()
            b1.set_title("Python Basics")
            b1.set_author("John Doe")
            print(f"Title: {b1.get_title()}, Author: {b1.get_author()}")
        
        elif choice == 8:
            a1 = Account()
            a1.deposit(100)
            a1.deposit(-50)
        
        elif choice == 9:
            p1 = PersonAge()
            p1.set_age(20)
            p1.set_age(-5)
        
        elif choice == 10:
            s1 = Student()
            s1.set_name("Charlie")
            s1.set_marks(85, 90, 95)
            s1.calculate_average()
            s1.display_grade()
        
        elif choice == 11:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()