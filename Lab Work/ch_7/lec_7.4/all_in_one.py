def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero!"

def square_root(n):
    import math
    return math.sqrt(n)

def sin_degrees(deg):
    import math
    return math.sin(math.radians(deg))

def count_vowels(string):
    vowels = 'aeiouAEIOU'
    return sum(string.count(vowel) for vowel in vowels)

def greet(name):
    return f"Hello, {name}! Welcome to the program."

def circle_area(radius):
    import math
    return math.pi * radius ** 2

def circle_perimeter(radius):
    import math
    return 2 * math.pi * radius

def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

def days_between_dates(date1, date2):
    from datetime import datetime
    date_format = "%Y-%m-%d"
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    return abs((d2 - d1).days)

def main():
    while True:
        print("\n=== Math Utility Menu ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square Root")
        print("6. Sin (Degrees)")
        print("7. Count Vowels")
        print("8. Greet")
        print("9. Circle Area")
        print("10. Circle Perimeter")
        print("11. Rectangle Area")
        print("12. Rectangle Perimeter")
        print("13. Days Between Dates")
        print("14. Exit")

        choice = input("Enter your choice (1-14): ")

        if choice == '1':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {add(a, b)}")

        elif choice == '2':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {subtract(a, b)}")

        elif choice == '3':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {multiply(a, b)}")

        elif choice == '4':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {divide(a, b)}")

        elif choice == '5':
            n = float(input("Enter number: "))
            print(f"Result: {square_root(n)}")

        elif choice == '6':
            deg = float(input("Enter degrees: "))
            print(f"Result: {sin_degrees(deg)}")

        elif choice == '7':
            string = input("Enter a string: ")
            print(f"Number of vowels: {count_vowels(string)}")

        elif choice == '8':
            name = input("Enter your name: ")
            print(greet(name))

        elif choice == '9':
            radius = float(input("Enter radius: "))
            print(f"Area: {circle_area(radius)}")

        elif choice == '10':
            radius = float(input("Enter radius: "))
            print(f"Perimeter: {circle_perimeter(radius)}")

        elif choice == '11':
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            print(f"Area: {rectangle_area(length, width)}")

        elif choice == '12':
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            print(f"Perimeter: {rectangle_perimeter(length, width)}")

        elif choice == '13':
            date1 = input("Enter first date (YYYY-MM-DD): ")
            date2 = input("Enter second date (YYYY-MM-DD): ")
            print(f"Days between: {days_between_dates(date1, date2)}")

        elif choice == '14':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 14.")

if __name__ == "__main__":
    main()