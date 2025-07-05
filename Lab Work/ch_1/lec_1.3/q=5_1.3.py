value = input("Enter a value: ")

a = value
b = value

print("\n--- Before changing 'a' ---")
print("a =", a)
print("b =", b)
print("Memory address of a:", id(a))
print("Memory address of b:", id(b))
print("Do 'a' and 'b' point to the same object?", id(a) == id(b))

new_value = input("\nEnter a new value to change 'a': ")

a = new_value

print("\n--- After changing 'a' ---")
print("a =", a)
print("b =", b)
print("Memory address of a:", id(a))
print("Memory address of b:", id(b))
print("Do 'a' and 'b' point to the same object now?", id(a) == id(b))
