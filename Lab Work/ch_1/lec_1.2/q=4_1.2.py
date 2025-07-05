integer = int(input("Enter an integer: "))
float = float(input("Enter a float: "))
string = input("Enter a string: ")
boolean = bool(input("Enter a boolean (True or False): "))
complex = complex(input("Enter a complex number: "))

print("Integer:", integer)
type_of_integer = type(integer).__name__
print("Float:", float)
type_of_float = type(float).__name__
print("String:", string)
type_of_string = type(string).__name__
print("Boolean:", boolean)
type_of_boolean = type(boolean).__name__
print("Complex:", complex)
type_of_complex = type(complex).__name__
