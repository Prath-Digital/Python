def cube_number(x):
    return x ** 3

def apply_function(numbers, func):
    return [func(x) for x in numbers]

# Test the program
numbers = [1, 2, 3, 4]
cubes = apply_function(numbers, cube_number)
print(f"Original numbers: {numbers}")
print(f"Cubes: {cubes}")