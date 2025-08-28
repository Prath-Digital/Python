# Introduction to NumPy

## 1. What is NumPy in Python, and why is it used in data science and numerical computing?
NumPy is a Python library that provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on them. It’s widely used in data science and numerical computing due to its efficiency in handling large datasets and performing complex computations.

## 2. Explain the key features of NumPy that differentiate it from Python's built-in lists.
- **Efficient Arrays**: NumPy arrays are more memory-efficient and faster than Python lists for numerical operations.
- **Multidimensional Support**: Handles 1D, 2D, and higher-dimensional arrays, unlike lists which are primarily 1D.
- **Vectorized Operations**: Allows element-wise operations without explicit loops.
- **Broadcasting**: Automatically handles operations on arrays of different shapes.

## 3. What are some common use cases of NumPy in scientific computing?
- Performing mathematical operations on large datasets.
- Implementing machine learning algorithms.
- Processing images and signals.
- Solving linear algebra problems.

## 4. How do you install NumPy in your Python environment?
Use the command `pip install numpy` in your terminal or command prompt to install NumPy.

# Working with Jupyter Notebook

## 5. What is Jupyter Notebook, and how is it different from a standard Python IDE?
Jupyter Notebook is an open-source web application for creating and sharing documents with live code, equations, and visualizations. It differs from a standard Python IDE (like PyCharm) by offering an interactive, cell-based environment ideal for data exploration, rather than just script development.

## 6. Explain the advantages of using Jupyter Notebook for data analysis and visualization.
- **Interactive Coding**: Run and test code in cells instantly.
- **Visual Integration**: Embed charts and plots directly using libraries like Matplotlib.
- **Documentation**: Combine code with markdown for clear explanations.
- **Sharing**: Easily share notebooks with others.

## 7. How do you create a new notebook and execute a Python cell in Jupyter Notebook?
- **Create**: Open Jupyter Notebook, click "New" > "Python 3" to start a new notebook.
- **Execute**: Write code in a cell and press `Shift + Enter` to run it.

## 8. What are the different types of cells in Jupyter Notebook, and what are they used for?
- **Code Cells**: For writing and executing Python code.
- **Markdown Cells**: For text, headings, and formatting documentation.
- **Raw Cells**: For unrendered text or code not meant to be executed.

# Working with Google Colab

## 9. What is Google Colab, and how does it differ from Jupyter Notebook?
Google Colab is a free, cloud-based Jupyter Notebook environment with pre-installed libraries and GPU support. It differs by offering free computational resources and seamless collaboration via Google Drive, without requiring local setup.

## 10. Explain how to upload files to Google Colab and access them in your code.
- **Upload**: Click the "Files" tab in Colab, then "Upload" to add files.
- **Access**: Use `open('filename.txt', 'r')` or load with `pd.read_csv('filename.csv')` in your code.

## 11. How can you install Python libraries in Google Colab that are not pre-installed?
Run `!pip install library_name` (e.g., `!pip install seaborn`) in a code cell to install additional libraries.

## 12. What are the advantages of using Google Colab for collaborative coding?
- **Real-Time Editing**: Multiple users can work simultaneously.
- **Cloud-Based**: Accessible from anywhere with an internet connection.
- **Free Resources**: Includes GPU/TPU support for heavy computations.

# Creation, Indexing, and Slicing of NumPy Arrays

## 13. How do you create a NumPy array from a Python list? Provide an example.
Use `np.array()` with a list. Example:
```python
import numpy as np
my_list = [1, 2, 3, 4]
my_array = np.array(my_list)
```

## 14. What is the difference between a 1D, 2D, and 3D NumPy array? Provide an example of each.
- **1D Array**: Single row. Example: `np.array([1, 2, 3])`
- **2D Array**: Matrix with rows and columns. Example: `np.array([[1, 2], [3, 4]])`
- **3D Array**: Layers of 2D arrays. Example: `np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])`

## 15. Explain how to access individual elements in a NumPy array using indexing.
Use square brackets with indices. Example: `array[0]` for a 1D array, or `array[0, 1]` for a 2D array (row 0, column 1).

## 16. What is slicing in NumPy, and how is it used to access subsets of an array?
Slicing extracts portions using `start:stop:step`. Example: `array[0:2]` gets elements 0 and 1; `array[0:2, 1:3]` gets a 2D subarray.

## 17. Write a program to create a 2D NumPy array and extract a subarray using slicing.
```python
import numpy as np
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
subarray = array_2d[0:2, 1:3]
```

## 18. How can you modify elements of a NumPy array using indexing and slicing?
- **Indexing**: `array[0] = 10` changes the first element.
- **Slicing**: `array[0:2] = [10, 20]` updates the first two elements.
Example:
```python
import numpy as np
array = np.array([1, 2, 3])
array[0] = 10  # Changes first element
array[1:3] = [20, 30]  # Changes second and third elements
```