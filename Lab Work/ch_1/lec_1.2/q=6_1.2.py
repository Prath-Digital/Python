print("Demonstration of logical operators (and, or, not)")

input1 = input("Enter first boolean value (True/False): ")
input2 = input("Enter second boolean value (True/False): ")

tf_values = ("true", "1", "yes", "y", "t")
bool1 = input1.strip().lower() in tf_values
bool2 = input2.strip().lower() in tf_values

print(f"\nYou entered: {bool1} and {bool2}")

print(f"{bool1} and {bool2} = {bool1 and bool2}")
print(f"{bool1} or {bool2} = {bool1 or bool2}")

print(f"not {bool1} = {not bool1}")
print(f"not {bool2} = {not bool2}")
