age = int(input("Enter your age: "))

if age >= 0:
    if age <= 12:
        print("You are a Child.")
    elif age <= 19:
        print("You are a Teenager.")
    elif age <= 59:
        print("You are an Adult.")
    else:
        print("You are a Senior.")
else:
    print("Invalid age entered.")
