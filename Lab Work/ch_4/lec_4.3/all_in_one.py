def display_1d_array(arr):
    for i in arr:
        print(i, end=" ")
    print()


def display_2d_array(arr):
    for row in arr:
        for elem in row:
            print(f"{elem:4}", end="")
        print()


def q1():
    arr = [1, 2, 3, 4, 5]
    print("Q1 - 1D Array:", end=" ")
    display_1d_array(arr)


def q2():
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Q2 - 2D Array (3x3):")
    display_2d_array(arr)


def q3():
    arr = [[1, 2], [3, 4]]
    print("Q3 - Original 2x2 Matrix:")
    display_2d_array(arr)
    transpose = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
    print("Transposed Matrix:")
    display_2d_array(transpose)


def q4():
    arr = [1, 2, 3, 4, 5]
    print("Q4 - Sum of 1D Array elements:", sum(arr))


def q5():
    arr = [[1, 2, 3], [4, 5, 6]]
    total = 0
    for row in arr:
        total += sum(row)
    print("Q5 - Sum of 2D Array elements:", total)


def q6():
    arr = [[1, 5, 3], [4, 2, 6]]
    flat = [x for row in arr for x in row]
    print("Q6 - Max:", max(flat), "Min:", min(flat))


def q7():
    arr = [1, 2, 3, 4]
    pos = int(input("Q7 - Enter position to insert: "))
    val = int(input("Enter value to insert: "))
    arr.insert(pos, val)
    print("Updated Array:", arr)


def q8():
    arr = [1, 2, 3, 4, 5]
    val = int(input("Q8 - Enter value to delete: "))
    if val in arr:
        arr.remove(val)
    print("Updated Array:", arr)


def q9():
    arr = [1, 2, 3, 4]
    idx = int(input("Q9 - Enter index to update: "))
    val = int(input("Enter new value: "))
    if 0 <= idx < len(arr):
        arr[idx] = val
    print("Updated Array:", arr)


def q10():
    arr = [1, 2, 3, 4, 5]
    val = int(input("Q10 - Enter value to search: "))
    print("Index:", arr.index(val) if val in arr else -1)


def q11():
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    print("Q11 - Concatenated Array:", arr1 + arr2)


def q12():
    arr = [5, 2, 8, 1, 9]
    arr.sort()
    print("Q12 - Sorted Array:", arr)


def q13():
    tuples = [(1, "z"), (3, "a"), (2, "b")]
    sorted_tuples = sorted(tuples, key=lambda x: x[1])
    print("Q13 - Sorted Tuples by second element:", sorted_tuples)


def q14():
    dicts = [{"name": "z", "age": 30}, {"name": "a", "age": 25}]
    sorted_dicts = sorted(dicts, key=lambda x: x["name"])
    print("Q14 - Sorted Dictionaries by name:", sorted_dicts)


def q15():
    arr = [3, 1, 4]
    arr_copy = arr.copy()
    arr.sort()
    sorted_arr = sorted(arr_copy)
    print("Q15 - In-place sort:", arr)
    print("Sorted (new list):", sorted_arr)


while True:
    print("\nMenu:")
    print("1. Q1: Create and display 1D array")
    print("2. Q2: Create and display 2D array")
    print("3. Q3: Transpose 2D array")
    print("4. Q4: Sum of 1D array")
    print("5. Q5: Sum of 2D array")
    print("6. Q6: Max and Min in 2D array")
    print("7. Q7: Insert element in 1D array")
    print("8. Q8: Delete element from 1D array")
    print("9. Q9: Update element in 1D array")
    print("10. Q10: Search element in 1D array")
    print("11. Q11: Concatenate two 1D arrays")
    print("12. Q12: Sort a list of integers")
    print("13. Q13: Sort tuples by second element")
    print("14. Q14: Sort dictionaries by specific key")
    print("15. Q15: Demonstrate sort() vs sorted()")
    print("0. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        q1()
    elif choice == 2:
        q2()
    elif choice == 3:
        q3()
    elif choice == 4:
        q4()
    elif choice == 5:
        q5()
    elif choice == 6:
        q6()
    elif choice == 7:
        q7()
    elif choice == 8:
        q8()
    elif choice == 9:
        q9()
    elif choice == 10:
        q10()
    elif choice == 11:
        q11()
    elif choice == 12:
        q12()
    elif choice == 13:
        q13()
    elif choice == 14:
        q14()
    elif choice == 15:
        q15()
    elif choice == 0:
        break
    else:
        print("Invalid choice! Please try again.")
