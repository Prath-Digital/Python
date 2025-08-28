# All-in-One Python Array and Sorting Guide

## Q1. How can you represent a 1D array using a list in Python? Provide an example.
**A1.** A 1D array can be represented using a simple list in Python. Example:
```python
my_array = [1, 2, 3, 4, 5]
```

## Q2. Explain how to create and access elements in a 2D array using nested lists in Python. Provide an example.
**A2.** A 2D array can be created using nested lists. Elements are accessed using two indices. Example:
```python
my_2d_array = [[1, 2, 3], [4, 5, 6]]
print(my_2d_array[0][1])  # Accesses 2
```

## Q3. Write a Python program to initialize a 2D array and print its elements row by row.
**A3.**
```python
my_2d_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in my_2d_array:
    print(row)
```

## Q4. What are the differences between arrays in Python and lists when used as 1D or 2D arrays?
**A4.** - **Lists** are built-in, flexible, and can hold mixed data types.  
  - **Arrays** (from `array` module) are more memory-efficient but require uniform data types.  
  - For 2D, lists use nested lists, while arrays can use `numpy` for better performance.

## Q5. What does CRUD stand for in the context of array operations?
**A5.** CRUD stands for Create, Read, Update, and Delete.

## Q6. Write a Python program to demonstrate the Create and Read operations on a 1D array using a list.
**A6.**
```python
# Create
my_array = [10, 20, 30, 40]
# Read
for item in my_array:
    print(item)
```

## Q7. Explain how to update a specific element in a 1D array (list). Provide an example.
**A7.** You can update an element by assigning a new value using its index. Example:
```python
my_array = [10, 20, 30]
my_array[1] = 25  # Updates 20 to 25
print(my_array)  # Output: [10, 25, 30]
```

## Q8. Write a program to delete an element from a 1D array by its index and by its value.
**A8.**
```python
my_array = [10, 20, 30, 40]
# Delete by index
my_array.pop(1)  # Removes 20
print(my_array)  # Output: [10, 30, 40]
# Delete by value
my_array.remove(30)  # Removes 30
print(my_array)  # Output: [10, 40]
```

## Q9. Write a menu-driven program to perform CRUD operations on a 1D array.
**A9.**
```python
my_array = []
while True:
    print("\n1. Create\n2. Read\n3. Update\n4. Delete\n5. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        val = int(input("Enter value: "))
        my_array.append(val)
    elif choice == 2:
        print(my_array)
    elif choice == 3:
        idx = int(input("Enter index: "))
        val = int(input("Enter new value: "))
        my_array[idx] = val
    elif choice == 4:
        idx = int(input("Enter index to delete: "))
        my_array.pop(idx)
    elif choice == 5:
        break
```

## Q10. What is the difference between the sort() method and the sorted() function in Python?
**A10.** - `sort()` modifies the list in-place and returns None.  
  - `sorted()` returns a new sorted list without changing the original.

## Q11. Write a Python program to sort a list of numbers in ascending and descending order using both sort() and sorted().
**A11.**
```python
my_list = [5, 2, 8, 1, 9]
# Using sort()
my_list.sort()  # Ascending
print("Ascending (sort):", my_list)
my_list.sort(reverse=True)  # Descending
print("Descending (sort):", my_list)
# Using sorted()
new_list = sorted(my_list)  # Ascending
print("Ascending (sorted):", new_list)
new_list = sorted(my_list, reverse=True)  # Descending
print("Descending (sorted):", new_list)
```

## Q12. Can sorted() be used with other collection datatypes like tuples or dictionaries? Provide examples.
**A12.** - **Tuples**: Yes, by converting to a list first. Example:
  ```python
  my_tuple = (5, 2, 8)
  sorted_list = sorted(my_tuple)
  print(sorted_list)  # Output: [2, 5, 8]
  ```
  - **Dictionaries**: Yes, by sorting keys or values. Example:
  ```python
  my_dict = {'a': 3, 'b': 1, 'c': 2}
  sorted_keys = sorted(my_dict.keys())
  print(sorted_keys)  # Output: ['a', 'b', 'c']
  ```

## Q13. What is the key parameter in the sorted() function? Write a program to sort a list of strings by their lengths.
**A13.** The `key` parameter specifies a function to customize the sort order. Example:
```python
my_strings = ["apple", "banana", "kiwi"]
sorted_strings = sorted(my_strings, key=len)
print(sorted_strings)  # Output: ['kiwi', 'apple', 'banana']
```