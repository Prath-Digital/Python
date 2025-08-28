def sum_and_product(*args):
    sum_result = sum(args)
    product_result = 1
    for num in args:
        product_result *= num
    return sum_result, product_result

# Test the function
result = sum_and_product(1, 2, 3, 4)
print(f"Sum: {result[0]}, Product: {result[1]}")