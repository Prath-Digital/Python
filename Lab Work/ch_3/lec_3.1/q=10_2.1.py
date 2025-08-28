# List example
my_list = [1, 2, 3]
my_list.append(4)
my_list.remove(2)
my_list[0] = 10
print("Updated list:", my_list)

# Tuple immutability explanation
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This will cause an error because tuples are immutable

print("Tuples cannot be modified after creation (no add/remove/replace).")
