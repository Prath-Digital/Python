int_var = int(input("Enter an integer (e.g. 10): "))
float_var = float(input("Enter a float number (e.g. 3.14): "))
string_var = input("Enter a string (e.g. Hello): ")

bool_input = input("Enter a boolean value (True or False): ")
if bool_input.lower() == 'true':
    bool_var = True
else:
    bool_var = False

list_input = input("Enter list items separated by commas (e.g. apple,banana,orange): ")
list_var = list_input.split(',')

tuple_input = input("Enter tuple items separated by commas (e.g. red,green,blue): ")
tuple_var = tuple(tuple_input.split(','))

dict_input = input("Enter dictionary items in key:value format separated by commas (e.g. name:John,age:30): ")
key_value1 = dict_input.split(',')[0].split(':')
key_value2 = dict_input.split(',')[1].split(':')
dict_var = {key_value1[0]: key_value1[1], key_value2[0]: key_value2[1]}

print()
print("----- Variable Details -----")
print("Integer -> Value:", int_var, ", Type:", type(int_var), ", Memory Address:", id(int_var))
print("Float -> Value:", float_var, ", Type:", type(float_var), ", Memory Address:", id(float_var))
print("String -> Value:", string_var, ", Type:", type(string_var), ", Memory Address:", id(string_var))
print("Boolean -> Value:", bool_var, ", Type:", type(bool_var), ", Memory Address:", id(bool_var))
print("List -> Value:", list_var, ", Type:", type(list_var), ", Memory Address:", id(list_var))
print("Tuple -> Value:", tuple_var, ", Type:", type(tuple_var), ", Memory Address:", id(tuple_var))
print("Dictionary -> Value:", dict_var, ", Type:", type(dict_var), ", Memory Address:", id(dict_var))
