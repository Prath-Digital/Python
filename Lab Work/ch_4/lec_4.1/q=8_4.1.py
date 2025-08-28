def filter_types(*args):
    strings = tuple(x for x in args if isinstance(x, str))
    numbers = tuple(x for x in args if isinstance(x, (int, float)) and not isinstance(x, bool))
    return strings, numbers

# Test the function
result = filter_types(1, "hello", 3.14, "world", 5)
print(f"Strings: {result[0]}")
print(f"Numbers: {result[1]}")