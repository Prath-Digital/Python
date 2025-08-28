# NumPy Questions and Answers

## 1. What is Boolean indexing in NumPy, and how is it used to filter arrays?
Boolean indexing in NumPy allows you to filter an array based on a condition. You create a Boolean mask (an array of True/False values) and use it to index the original array, returning only the elements where the mask is True.

## 2. Write an example of using Boolean indexing to filter even numbers from a NumPy array.
```python
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
even_numbers = arr[arr % 2 == 0]
```

## 3. What is the difference between Boolean indexing and masking in NumPy?
Boolean indexing and masking are similar, but masking often implies creating a Boolean array to apply operations (like replacing values), while Boolean indexing directly selects elements based on the mask. Masking can be part of Boolean indexing but is more general.

## 4. How can you use masking to replace all negative values in a NumPy array with 0?
```python
import numpy as np
arr = np.array([-1, 2, -3, 4, -5])
arr[arr < 0] = 0
```

## 5. Explain how reshaping works in NumPy arrays. What does the reshape() function do?
Reshaping changes the shape of an array without changing its data. The `reshape()` function reorganizes the elements into a new shape, provided the total number of elements remains the same.

## 6. Provide an example of reshaping a 1D NumPy array into a 2D array of shape (3, 2).
```python
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape(3, 2)
```

## 7. What will happen if you try to reshape an array to an incompatible shape? Give an example.
If the new shape is incompatible (e.g., total elements don't match), NumPy raises a `ValueError`. Example:
```python
import numpy as np
arr = np.array([1, 2, 3])
arr.reshape(2, 2)  # Raises ValueError
```

## 8. What is broadcasting in NumPy, and why is it useful in array arithmetic?
Broadcasting allows NumPy to perform operations on arrays of different shapes by automatically expanding the smaller array to match the larger one. It’s useful for efficient array arithmetic without explicit loops.

## 9. Give an example where broadcasting is used to add a 1D array to a 2D array.
```python
import numpy as np
arr_2d = np.array([[1, 2], [3, 4]])
arr_1d = np.array([10, 20])
result = arr_2d + arr_1d
```

## 10. What are the rules that NumPy follows to perform broadcasting between arrays of different shapes?
NumPy compares array dimensions from the end. Arrays are compatible if:
- They have the same size in a dimension, or
- One of them has size 1 in that dimension, which is stretched.

## 11. How can broadcasting make your code more efficient than using loops?
Broadcasting avoids explicit loops by leveraging optimized C-level operations, reducing overhead and making code faster, especially for large arrays.

## 12. Explain the difference between broadcasting and tiling in the context of NumPy.
Broadcasting automatically adjusts array shapes for operations, while tiling explicitly repeats an array to a desired shape using `np.tile()`. Broadcasting is more memory-efficient as it doesn’t create new data.