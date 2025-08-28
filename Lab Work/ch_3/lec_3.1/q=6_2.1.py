user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
