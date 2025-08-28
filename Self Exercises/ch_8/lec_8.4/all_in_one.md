# Pandas Questions and Answers

## 1. What is the Pandas library in Python? Explain its significance in data analysis.
Pandas is an open-source Python library that provides high-performance, easy-to-use data structures and data analysis tools. Its significance in data analysis lies in its ability to handle large datasets, perform data manipulation, cleaning, and analysis efficiently with its primary data structures: Series and DataFrame.

## 2. Differentiate between a Pandas Series and a DataFrame with suitable examples.
- **Series**: A one-dimensional labeled array capable of holding any data type. Example: `pd.Series([1, 2, 3], index=['a', 'b', 'c'])` creates a Series with labeled indices.
- **DataFrame**: A two-dimensional labeled data structure with columns of potentially different types. Example: `pd.DataFrame({'A': [1, 2], 'B': [3, 4]})` creates a DataFrame with two columns.

## 3. How do you create a Pandas DataFrame from a dictionary? Write the code.
import pandas as pd
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)

## 4. Write code to create a Series from a Python list. Display its type and contents.
import pandas as pd
my_list = [10, 20, 30, 40]
series = pd.Series(my_list)
print(type(series))
print(series)

## 5. What are the different ways to explore a DataFrame's structure and summary?
- Use `.head()` to view the first few rows.
- Use `.info()` to get a concise summary of the DataFrame.
- Use `.describe()` to get statistical summary of numerical columns.

## 6. Explain the use of `.head()`, `.tail()`, and `.info()` methods in Pandas with examples.
- **.head()**: Returns the first 5 rows. Example: `df.head()` shows the top 5 rows.
- **.tail()**: Returns the last 5 rows. Example: `df.tail()` shows the bottom 5 rows.
- **.info()**: Provides a summary of the DataFrame including data types and non-null values. Example: `df.info()`.

## 7. What are some common operations that can be performed on a DataFrame?
- Adding/removing columns or rows.
- Filtering data based on conditions.
- Grouping and aggregating data.
- Merging or joining DataFrames.

## 8. Write a program to perform column-wise and row-wise addition of two DataFrames.
import pandas as pd
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
# Column-wise addition
col_sum = df1 + df2
# Row-wise addition
row_sum = df1.add(df2, axis=1)

## 9. How can you select specific rows and columns from a DataFrame using `loc` and `iloc`?
- **loc**: Label-based selection. Example: `df.loc[0:2, 'A']` selects rows 0 to 2 and column 'A'.
- **iloc**: Integer-based selection. Example: `df.iloc[0:2, 0]` selects rows 0 to 1 and column 0.

## 10. What is the difference between `df['column']` and `df[['column']]`?
- `df['column']`: Returns a Series with the specified column.
- `df[['column']]`: Returns a DataFrame with the specified column(s).

## 11. Write code to add a new column to a DataFrame and fill it with default values.
import pandas as pd
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df['C'] = 0  # Adds new column 'C' with default value 0

## 12. How do you apply functions on DataFrame columns using `.apply()` method?
You can apply a function to each column using `.apply()`. Example:
import pandas as pd
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df['A'] = df['A'].apply(lambda x: x * 2)