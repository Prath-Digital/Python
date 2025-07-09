a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, **, /): ")

match operator:
    case '+':
        print("Result:", a + b)
    case '-':
        print("Result:", a - b)
    case '**':
        print("Result:", a ** b)
    case '/':
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operator.")
