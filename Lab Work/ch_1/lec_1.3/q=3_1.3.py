user_input = input("Enter True or False: ")
boolean_value = user_input.lower() == "true"

bool_int = int(boolean_value)
bool_str = str(boolean_value)

print("Boolean value:", boolean_value)
print("Integer representation:", bool_int)
print("String representation:", bool_str)