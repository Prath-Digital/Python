def set_operations():
    nums = input("Enter integers separated by spaces (e.g., 1 2 3 4): ")
    unique_numbers = set(map(int, nums.split()))
    add_num = int(input("Enter an integer to add to the set: "))
    remove_num = int(input("Enter an integer to remove from the set: "))
    unique_numbers.add(add_num)
    unique_numbers.discard(remove_num)
    print("Final set (duplicates auto-removed):", unique_numbers)


def dictionary_operations():
    name = input("Enter name (string): ")
    age = int(input("Enter age (integer): "))
    city = input("Enter city (string): ")
    person = {"name": name, "age": age, "city": city}
    new_key = input("Enter a new key to add (string): ")
    new_value = input(f"Enter value for '{new_key}' (string): ")
    person[new_key] = new_value
    update_key = input("Enter a key to update (string): ")
    update_value = input(f"Enter new value for '{update_key}' (string or number): ")
    person[update_key] = int(update_value) if update_value.isdigit() else update_value
    remove_key = input("Enter a key to remove (string): ")
    person.pop(remove_key, None)
    print("Updated dictionary:", person)


def remove_duplicates_from_list():
    data = input("Enter integers separated by spaces (e.g., 1 2 2 3): ")
    lst = list(map(int, data.split()))
    print("Unique numbers:", set(lst))


def most_expensive_product():
    n = int(input("Enter number of products (integer): "))
    products = {}
    for _ in range(n):
        name = input("Enter product name (string): ")
        price = float(input(f"Enter price for {name} (float): "))
        products[name] = price
    max_product = max(products.items(), key=lambda x: x[1])
    print("Most expensive product:", max_product)


def char_frequency():
    text = input("Enter a string: ")
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    print("Character frequencies:", freq)


def factorial_program():
    n = int(input("Enter a number to calculate factorial (integer): "))
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(f"Factorial of {n} is:", result)


def rectangle_area():
    def area(length, width):
        return length * width

    l = float(input("Enter length (float): "))
    w = float(input("Enter width (float): "))
    print("Area of rectangle:", area(l, w))


def type_conversion():
    lst = input("Enter list items separated by spaces (e.g., a b c): ").split()
    print("List to Set:", set(lst))
    print("List to Tuple:", tuple(lst))
    tup = tuple(
        input("Enter tuple elements separated by spaces (e.g., x y z): ").split()
    )
    print("Tuple to List:", list(tup))
    st = set(input("Enter set elements separated by spaces (e.g., red blue): ").split())
    print("Set to List:", list(st))
    print("Set to Tuple:", tuple(st))


def convert_csv_string():
    csv = input("Enter comma-separated values (e.g., 1,2,3): ")
    items = csv.split(",")
    print("As List:", list(items))
    print("As Set:", set(items))
    print("As Tuple:", tuple(items))


def dict_key_value_conversion():
    n = int(input("Enter number of key-value pairs: "))
    d = {}
    for _ in range(n):
        k = input("Key (string): ")
        v = input("Value (string): ")
        d[k] = v
    print("Keys as List:", list(d.keys()))
    print("Keys as Set:", set(d.keys()))
    print("Values as List:", list(d.values()))
    print("Values as Tuple:", tuple(d.values()))


def remove_list_duplicates_ordered():
    data = input("Enter list with duplicates (e.g., a b a c): ").split()
    result = list(dict.fromkeys(data))
    print("Ordered unique list:", result)


def set_to_square_dict():
    nums = input("Enter unique integers (e.g., 1 2 3): ")
    s = set(map(int, nums.split()))
    d = {x: x**2 for x in s}
    print("Dictionary of squares:", d)


def show_menu():
    print("\n=== Python Task Menu ===")
    print("1. Set operations (add/remove)")
    print("2. Dictionary operations")
    print("3. Remove duplicates from list")
    print("4. Find most expensive product")
    print("5. Character frequency count")
    print("6. Factorial of a number")
    print("7. Area of a rectangle")
    print("8. Type conversions (list, set, tuple)")
    print("9. Convert comma-separated string")
    print("10. Dictionary keys/values conversion")
    print("11. Remove duplicates and retain order")
    print("12. Set to square dictionary")
    print("0. Exit")


while True:
    show_menu()
    choice = input("Enter your choice (0-12): ")
    if choice == "1":
        set_operations()
    elif choice == "2":
        dictionary_operations()
    elif choice == "3":
        remove_duplicates_from_list()
    elif choice == "4":
        most_expensive_product()
    elif choice == "5":
        char_frequency()
    elif choice == "6":
        factorial_program()
    elif choice == "7":
        rectangle_area()
    elif choice == "8":
        type_conversion()
    elif choice == "9":
        convert_csv_string()
    elif choice == "10":
        dict_key_value_conversion()
    elif choice == "11":
        remove_list_duplicates_ordered()
    elif choice == "12":
        set_to_square_dict()
    elif choice == "0":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
