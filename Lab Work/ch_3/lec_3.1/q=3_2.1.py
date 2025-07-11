text = input("Enter a string: ")
reversed_text = text[::-1]
print(f"Reversed string: {reversed_text}")
if text == reversed_text:
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")
