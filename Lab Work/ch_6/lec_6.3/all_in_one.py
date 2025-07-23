def menu_udf():
    choice = input("Enter choice (1-8): ")
    if choice == "1":
        num = float(input("Enter a number: "))
        if num < 0:
            raise ValueError("Negative number not allowed")
    elif choice == "2":

        def check_even(n):
            if not isinstance(n, int):
                raise TypeError("Input must be an integer")
            if n % 2 != 0:
                raise ValueError("Number must be even")

        check_even(eval(input("Enter a number: ")))
    elif choice == "3":
        age = int(input("Enter your age: "))
        assert age > 18, "Age must be above 18"
    elif choice == "4":

        def check_palindrome(s):
            assert s != "", "Input string cannot be empty"

        check_palindrome(input("Enter a string: "))
    elif choice == "5":

        class InsufficientBalanceError(Exception):
            pass

        def withdraw(amount):
            balance = float(input("Enter account balance: "))
            if amount > balance:
                raise InsufficientBalanceError("Withdrawal amount exceeds balance")
            print("Withdrawal successful")

        amount = float(input("Enter withdrawal amount: "))
        withdraw(amount)
    elif choice == "6":

        class InvalidEmailError(Exception):
            pass

        def validate_email(email):
            if "@" not in email or not email.endswith((".com", ".org")):
                raise InvalidEmailError("Invalid email format")

        validate_email(input("Enter email: "))
    elif choice == "7":

        class InvalidGradeError(Exception):
            pass

        grade = float(input("Enter grade: "))
        assert grade != "", "Grade cannot be empty"
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100")
        if grade < 40:
            raise InvalidGradeError("Failing grade")
    elif choice == "8":

        class HighTemperatureError(Exception):
            pass

        temp = input("Enter temperature: ")
        if not isinstance(eval(temp), (int, float)):
            raise TypeError("Input must be a number")
        temp_val = float(temp)
        assert -273 <= temp_val <= 10000, "Temperature out of reasonable range"
        if temp_val > 1000:
            raise HighTemperatureError(
                "Temperature exceeds 1000°C, unrealistic for common applications"
            )


menu_udf()
