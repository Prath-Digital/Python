# Python Collections & Comments – Q&A

### Q1: What is a set in Python, and how does it differ from other collection datatypes?

A **set** is an unordered collection of unique elements in Python. Unlike lists or tuples, sets do not allow duplicate values. Sets are mutable but do not support indexing or slicing.

---

### Q2: Explain the concept of a dictionary in Python. How is it structured, and what makes it unique?

A **dictionary** is a collection of key-value pairs. It is unordered, mutable, and indexed by keys. Keys must be unique and immutable, while values can be of any type.

```python
example = {'name': 'Alice', 'age': 25}
```

---

### Q3: Write a program to demonstrate basic operations on a set (add, remove, union, intersection).

```python
a = {1, 2, 3}
b = {3, 4, 5}

a.add(6)
a.remove(2)

print("Union:", a | b)
print("Intersection:", a & b)
```

---

### Q4: How can you add, update, and delete key-value pairs in a dictionary? Provide examples.

```python
d = {'name': 'John'}
d['age'] = 30        # Add
d['name'] = 'Alice'  # Update
del d['age']         # Delete
```

---

### Q5: Discuss the differences between sets and dictionaries in terms of use cases and functionality.

- **Sets** store unique values, best for membership tests and mathematical operations.
- **Dictionaries** store key-value pairs, suitable for structured data and fast lookup by key.

---

### Q6: What are comments in Python, and why are they important?

**Comments** are ignored by the Python interpreter and used to explain code. They improve readability and maintainability.

---

### Q7: Explain the difference between single-line and multi-line comments in Python. Provide examples.

```python
# Single-line comment

"""
Multi-line
comment
"""
```

---

### Q8: How can docstrings be used as comments? Write a program to demonstrate their use in a function.

```python
def greet():
    """This function greets the user."""
    print("Hello!")

print(greet.__doc__)
```

---

### Q9: What is type casting in Python, and how can it be applied to collection datatypes like sets, lists, and dictionaries?

**Type casting** converts one data type to another. You can cast a list to a set to remove duplicates or cast a set to a list to enable indexing.

```python
s = set([1, 2, 3])
l = list(s)
```

---

### Q10: What is a Frozen Set? Explain how to create it.

A **frozenset** is an immutable version of a set.

```python
f = frozenset([1, 2, 3])
```

---

### Q11: Explain the difference between a set and a frozenset.

- **Set**: Mutable, elements can be added/removed.
- **Frozenset**: Immutable, elements cannot be changed.

---

### Q12: Write a program to convert a list into a set and a set into a list using type-casting constructors.

```python
l = [1, 2, 2, 3]
s = set(l)      # List to Set
l2 = list(s)    # Set to List
```

---

### Q13: What is the del keyword in Python, and how is it used to delete variables, list items, or dictionary keys? Provide examples.

```python
x = 10
del x

lst = [1, 2, 3]
del lst[1]

d = {'a': 1, 'b': 2}
del d['a']
```

---

### Q14: Explain the difference between using the del keyword and the clear() method for removing elements from collections.

- `del` removes a specific item or variable.
- `clear()` removes all elements from a collection (like list, dict, set) but retains the object.

```python
d = {'a': 1, 'b': 2}
del d['a']   # Removes specific key
d.clear()    # Empties the dictionary
```
