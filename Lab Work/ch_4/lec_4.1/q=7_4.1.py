def print_names(*args):
    if not args:
        print("The list of names is empty!")
    else:
        for name in args:
            print(name)

# Test the function
print_names("Alice", "Bob", "Charlie")
print("\nTesting empty list:")
print_names()