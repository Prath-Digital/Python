def square_numbers(numbers):
    return [x ** 2 for x in numbers]

# Test the function
input_list = [1, 2, 3, 4, 5]
squared_list = square_numbers(input_list)
print(f"Original list: {input_list}")
print(f"Squared list: {squared_list}")