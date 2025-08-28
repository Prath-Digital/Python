def char_frequency(text):
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

# Test the function
input_string = input("Enter a string: ")
result = char_frequency(input_string)
print(f"Character frequency: {result}")