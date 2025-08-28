for i in range(1, 51):
    if i % 2 == 0 and i % 3 == 0:
        print(f"{i} is divisible by both 2 and 3")
    elif i % 2 == 0:
        print(f"{i} is divisible by 2")
    elif i % 3 == 0:
        print(f"{i} is divisible by 3")
