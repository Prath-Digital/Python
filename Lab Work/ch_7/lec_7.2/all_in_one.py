import math
import random
import uuid
import time

def premium_menu():
    width = 60
    title = "Premium Python Utility Menu"
    lines = [
        "Q1  > Square root, factorial, and power",
        "Q2  > Area of circle and natural logarithm",
        "Q3  > Trigonometric functions",
        "Q4  > Ceiling, floor, and absolute value",
        "Q5  > Generate 10 random integers",
        "Q6  > Simulate dice roll and shuffle list",
        "Q7  > Random choice from list",
        "Q8  > Rock-Paper-Scissor game",
        "Q9  > Generate random UUID",
        "Q10 > Create student IDs with unique UUIDs",
        "Q11 > Compare two UUIDs",
        "Q12 > Simulate e-commerce order IDs with UUID",
        " 0  > Exit"
    ]
    print("\n" + "╔" + "═" * (width - 2) + "╗")
    pad = (width - 2 - len(title)) // 2
    print("║" + " " * pad + title + " " * (width - 2 - len(title) - pad) + "║")
    print("╠" + "═" * (width - 2) + "╣")
    for line in lines:
        print("║ " + line + " " * (width - 3 - len(line)) + "║")
    print("╚" + "═" * (width - 2) + "╝")
    return input("Enter your choice (Q1-Q12 or 0): ")

def menu():
    print("\n=== Menu ===")
    print("Q1: Square root, factorial, and power of numbers")
    print("Q2: Area of circle and natural logarithm")
    print("Q3: Trigonometric functions")
    print("Q4: Ceiling, floor, and absolute value")
    print("Q5: Generate 10 random integers")
    print("Q6: Simulate dice roll and shuffle list")
    print("Q7: Random choice from list")
    print("Q8: Rock-Paper-Scissor game")
    print("Q9: Generate random UUID")
    print("Q10: Create student IDs with unique UUIDs")
    print("Q11: Compare two UUIDs")
    print("Q12: Simulate e-commerce order IDs with UUIDs")
    print("0: Exit")
    return input("Enter your choice (Q1-Q12 or 0): ")

def q1():
    num = float(input("Enter a number: "))
    print(f"Square root: {math.sqrt(num)}")
    print(f"Factorial: {math.factorial(int(num)) if num >= 0 and num.is_integer() else 'Not defined'}")
    power = float(input("Enter power: "))
    print(f"Power: {math.pow(num, power)}")

def q2():
    radius = float(input("Enter radius: "))
    print(f"Area of circle: {math.pi * radius * radius}")
    num = float(input("Enter a number: "))
    print(f"Natural log: {math.log(num)}")

def q3():
    angle = float(input("Enter angle in degrees: "))
    angle_rad = math.radians(angle)
    print(f"sin({angle}) = {math.sin(angle_rad)}")
    print(f"cos({angle}) = {math.cos(angle_rad)}")
    print(f"tan({angle}) = {math.tan(angle_rad)}")

def q4():
    num = float(input("Enter a number: "))
    print(f"Ceiling: {math.ceil(num)}")
    print(f"Floor: {math.floor(num)}")
    print(f"Absolute value: {math.fabs(num)}")

def q5():
    numbers = [random.randint(1, 100) for _ in range(10)]
    print(f"Random integers: {numbers}")

def q6():
    print(f"Dice roll: {random.randint(1, 6)}")
    numbers = list(range(1, 6))
    random.shuffle(numbers)
    print(f"Shuffled list: {numbers}")

def q7():
    items = input("Enter items (space-separated): ").split()
    print(f"Random choice: {random.choice(items)}")

def q8():
    choices = ["rock", "paper", "scissor"]
    while True:
        player = input("Enter your choice (rock/paper/scissor) or 'quit': ").lower()
        if player == 'quit':
            break
        if player not in choices:
            print("Invalid choice!")
            continue
        computer = random.choice(choices)
        print(f"Computer chose: {computer}")
        if player == computer:
            print("It's a tie!")
        elif (player == "rock" and computer == "scissor") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissor" and computer == "paper"):
            print("You win!")
        else:
            print("Computer wins!")

def q9():
    print(f"Random UUID: {uuid.uuid4()}")
    namespace = uuid.NAMESPACE_DNS
    name = input("Enter a name for UUID: ")
    print(f"UUID with namespace: {uuid.uuid5(namespace, name)}")

def q10():
    students = {}
    num_students = int(input("Enter number of students: "))
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        students[student_id] = uuid.uuid4()
    for sid, uid in students.items():
        print(f"Student ID: {sid}, UUID: {uid}")

def q11():
    uid1 = uuid.uuid4()
    uid2 = uuid.uuid4()
    print(f"UUID1: {uid1}")
    print(f"UUID2: {uid2}")
    print(f"Are they equal? {uid1 == uid2}")

def q12():
    orders = {}
    num_orders = int(input("Enter number of orders: "))
    for _ in range(num_orders):
        order_id = input("Enter order ID: ")
        orders[order_id] = uuid.uuid4()
    for oid, uid in orders.items():
        print(f"Order ID: {oid}, UUID: {uid}")

while True:
    choice = premium_menu()
    if choice == "0":
        print("Goodbye!")
        print("Exiting the program...")
        time.sleep(random.randint(1, 6))
        break
    elif choice == "Q1":
        q1()
    elif choice == "Q2":
        q2()
    elif choice == "Q3":
        q3()
    elif choice == "Q4":
        q4()
    elif choice == "Q5":
        q5()
    elif choice == "Q6":
        q6()
    elif choice == "Q7":
        q7()
    elif choice == "Q8":
        q8()
    elif choice == "Q9":
        q9()
    elif choice == "Q10":
        q10()
    elif choice == "Q11":
        q11()
    elif choice == "Q12":
        q12()
    else:
        print("Invalid choice! Please try again.")