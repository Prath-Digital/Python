# NumPy Questions and Answers

## Mathematical Operations

### 1. What are element-wise operations in NumPy arrays?
Element-wise operations in NumPy allow you to perform operations on corresponding elements of arrays. For example, adding two arrays results in the sum of each pair of elements.

### 2. How does broadcasting work in NumPy? Give an example.
Broadcasting allows NumPy to perform operations on arrays of different shapes by automatically expanding the smaller array to match the shape of the larger one. Example: Adding a scalar to an array (e.g., `a + 5` where `a` is an array).

### 3. What are the differences between np.add(), np.subtract(), np.multiply(), and np.divide()?
These are ufuncs (universal functions) in NumPy that perform element-wise addition, subtraction, multiplication, and division, respectively. They are similar to `+`, `-`, `*`, and `/` but provide more control and handle edge cases like division by zero.

### 4. Explain how to perform matrix multiplication using NumPy.
Matrix multiplication can be performed using `np.dot()` or the `@` operator. Example: `np.dot(a, b)` or `a @ b` where `a` and `b` are matrices.

### 5. What is the difference between * and @ operators in NumPy?
The `*` operator performs element-wise multiplication, while the `@` operator performs matrix multiplication.

## Combining and Splitting Arrays

### 6. What functions are used to combine arrays horizontally and vertically?
Use `np.hstack()` for horizontal stacking and `np.vstack()` for vertical stacking.

### 7. Explain the difference between np.concatenate(), np.vstack(), and np.hstack().
- `np.concatenate()` joins arrays along an existing axis.
- `np.vstack()` stacks arrays vertically (along rows).
- `np.hstack()` stacks arrays horizontally (along columns).

### 8. How can you split a NumPy array into multiple smaller arrays?
Use `np.split()`, `np.array_split()`, `np.hsplit()`, or `np.vsplit()` depending on the splitting direction and requirements.

### 9. What is the difference between np.split() and np.array_split()?
`np.split()` requires the split to be exact (divisors must evenly divide the axis), while `np.array_split()` allows for uneven splits.

### 10. How would you reshape and then split a 2D array into rows and columns?
Reshape using `np.reshape()` and then split using `np.hsplit()` for columns or `np.vsplit()` for rows. Example: `np.vsplit(np.reshape(a, (new_rows, -1)), num_splits)`.

## Search, Sort, Aggregating & Statistical Functions

### 11. How do you search for an element in a NumPy array?
Use `np.where()` to find indices where a condition is true, e.g., `np.where(a == value)`.

### 12. What is the purpose of np.where() function?
`np.where()` returns indices where a condition is met or can choose elements from arrays based on a condition.

### 13. How does the np.sort() function work? How is it different from Python's built-in sorted()?
`np.sort()` sorts a NumPy array in-place or returns a sorted copy along an axis. `sorted()` works on Python lists and returns a new list, not optimized for NumPy arrays.

### 14. What are the key aggregate functions in NumPy? Explain with examples.
Key functions include `np.sum()`, `np.mean()`, `np.max()`, `np.min()`. Example: `np.sum(a)` adds all elements in array `a`.

### 15. How do you calculate the mean, median, standard deviation, and variance in NumPy?
- Mean: `np.mean(a)`
- Median: `np.median(a)`
- Standard deviation: `np.std(a)`
- Variance: `np.var(a)`