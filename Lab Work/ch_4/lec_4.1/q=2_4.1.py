def calculate_factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Test the function
number = int(input("Enter a number: "))
print(f"Factorial of {number} is {calculate_factorial(number)}")