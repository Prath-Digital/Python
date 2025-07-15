global_count = 0
global_sum = 0
username = "Guest"


def menu():
    print("\033[1;34m\n=== Programming Challenges Menu ===\033[0m")
    print("\033[1;32mQ1. Factorial (Recursive)\033[0m")
    print("\033[1;32mQ2. Fibonacci (Recursive)\033[0m")
    print("\033[1;32mQ3. Reverse String (Recursive)\033[0m")
    print("\033[1;32mQ4. Sum of Digits (Recursive)\033[0m")
    print("\033[1;32mQ5. Prime Numbers (Recursive)\033[0m")
    print("\033[1;32mQ6. Square List (Lambda)\033[0m")
    print("\033[1;32mQ7. Filter Odd Numbers (Lambda)\033[0m")
    print("\033[1;32mQ8. Largest of Three (Lambda)\033[0m")
    print("\033[1;32mQ9. Function Call Counter (Global)\033[0m")
    print("\033[1;32mQ10. Sum Tracker (Global)\033[0m")
    print("\033[1;32mQ11. Update Username (Global)\033[0m")
    print("\033[1;32mQ12. Global Variable Increment\033[0m")
    print("\033[1;32mQ13. Local vs Global Demo\033[0m")
    print("\033[1;32mQ14. Sum, Max, Min of List\033[0m")
    print("\033[1;32mQ15. Rectangle Area and Perimeter\033[0m")
    print("\033[1;32mQ16. Square and Cube Tuple\033[0m")
    print("\033[1;32mQ17. Split Vowels and Consonants\033[0m")
    print("\033[1;32mQ18. Split Words by Vowels/Consonants\033[0m")
    print("\033[1;31m0. Exit\033[0m")
    choice = int(input("Enter your choice (0-18): "))
    return choice


def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


def sum_of_digits(n):
    if n < 0:
        n = -n
    if n < 10:
        return n
    return (n % 10) + sum_of_digits(n // 10)


def is_prime(n, divisor=2):
    if n < 2:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor + 1)


def print_primes(start, end):
    if start > end:
        return
    if is_prime(start):
        print(start, end=" ")
    print_primes(start + 1, end)


square_lambda = lambda x: list(map(lambda y: y * y, x))

filter_odd = lambda x: list(filter(lambda y: y % 2 != 0, x))

largest_lambda = lambda a, b, c: a if a >= b and a >= c else b if b >= c else c


def count_call():
    global global_count
    global_count += 1
    return global_count


def update_sum(num):
    global global_sum
    global_sum += num
    return global_sum


def update_username():
    global username
    username = input("Enter new username: ")
    return username


def initialize_global():
    global global_var
    global_var = 0


def increment_global(value):
    global global_var
    global_var += value
    return global_var


def demo_variables():
    global global_name
    local_name = "Local"
    global_name = "Global"
    print(f"Local name: {local_name}, Global name: {global_name}")


def analyze_list(numbers):
    if not numbers:
        return None, None, None
    return sum(numbers), max(numbers), min(numbers)


def rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


def square_cube(num):
    return (num * num, num * num * num)


def split_vowels_consonants(s):
    vowels = "".join(c for c in s.lower() if c in "aeiou")
    consonants = "".join(c for c in s.lower() if c not in "aeiou" and c.isalpha())
    return vowels, consonants


def split_words_by_vowel(words):
    vowel_start = [w for w in words if w[0].lower() in "aeiou"]
    consonant_start = [w for w in words if w[0].lower() not in "aeiou"]
    return vowel_start, consonant_start


while True:
    choice = menu()
    if choice == 0:
        print("Goodbye!")
        break
    elif choice == 1:
        n = int(input("Enter a number for factorial: "))
        print(f"Factorial of {n} is {factorial(n)}")
    elif choice == 2:
        n = int(input("Enter a number for Fibonacci: "))
        print(f"Fibonacci of {n} is {fibonacci(n)}")
    elif choice == 3:
        s = input("Enter a string to reverse: ")
        print(f"Reversed string: {reverse_string(s)}")
    elif choice == 4:
        n = int(input("Enter a number for sum of digits: "))
        print(f"Sum of digits until single digit: {sum_of_digits(n)}")
    elif choice == 5:
        start = int(input("Enter start number: "))
        end = int(input("Enter end number: "))
        print(f"Prime numbers between {start} and {end}: ")
        print_primes(start, end)
    elif choice == 6:
        nums = list(map(int, input("Enter numbers separated by space: ").split()))
        print(f"Squares: {square_lambda(nums)}")
    elif choice == 7:
        nums = list(map(int, input("Enter numbers separated by space: ").split()))
        print(f"Odd numbers: {filter_odd(nums)}")
    elif choice == 8:
        a, b, c = map(int, input("Enter three numbers separated by space: ").split())
        print(f"Largest number: {largest_lambda(a, b, c)}")
    elif choice == 9:
        count_call()
        print(f"Function called {global_count} times")
    elif choice == 10:
        num = int(input("Enter a number to add to sum: "))
        print(f"Running sum: {update_sum(num)}")
    elif choice == 11:
        print(f"Updated username: {update_username()}")
    elif choice == 12:
        initialize_global()
        value = int(input("Enter value to increment by: "))
        print(f"Incremented value: {increment_global(value)}")
    elif choice == 13:
        demo_variables()
    elif choice == 14:
        nums = list(map(int, input("Enter numbers separated by space: ").split()))
        sum_val, max_val, min_val = analyze_list(nums)
        print(f"Sum: {sum_val}, Max: {max_val}, Min: {min_val}")
    elif choice == 15:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area, perimeter = rectangle_properties(length, width)
        print(f"Area: {area}, Perimeter: {perimeter}")
    elif choice == 16:
        num = int(input("Enter a number: "))
        square, cube = square_cube(num)
        print(f"Square: {square}, Cube: {cube}")
    elif choice == 17:
        s = input("Enter a string: ")
        vowels, consonants = split_vowels_consonants(s)
        print(f"Vowels: {vowels}, Consonants: {consonants}")
    elif choice == 18:
        words = input("Enter words separated by space: ").split()
        vowel_words, consonant_words = split_words_by_vowel(words)
        print(f"Words starting with vowels: {vowel_words}")
        print(f"Words starting with consonants: {consonant_words}")
    else:
        print("Invalid choice! Please try again.")
