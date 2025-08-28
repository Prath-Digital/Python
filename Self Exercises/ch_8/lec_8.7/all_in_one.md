# Pivoting

1. **What is pivoting in Pandas?**Pivoting in Pandas is a technique to reshape a DataFrame by rotating its rows into columns based on specific column values, making it easier to analyze data from a different perspective.
2. **How does the pivot() function differ from pivot_table() in Pandas?**The `pivot()` function reshapes data without aggregation, requiring unique index/column combinations, while `pivot_table()` allows aggregation (e.g., sum, mean) when there are duplicate entries.
3. **What are the necessary conditions for pivoting a DataFrame?**The DataFrame must have unique combinations of the index and column values specified for pivoting; otherwise, an error is raised unless handled with aggregation.
4. **Explain with an example how to pivot a DataFrame using the pivot() function.**Consider a DataFrame with sales data:

   ```python
   import pandas as pd
   df = pd.DataFrame({'Date': ['2023-01-01', '2023-01-01', '2023-01-02'],
                      'City': ['NY', 'LA', 'NY'],
                      'Sales': [100, 200, 150]})
   pivoted = df.pivot(index='Date', columns='City', values='Sales')
   ```

   This transforms the data into a table with Dates as rows and Cities as columns.
5. **How does aggregation play a role in pivot_table()?**
   Aggregation in `pivot_table()` combines duplicate entries (e.g., using `aggfunc='sum'`) to summarize data, which is essential when pivoting data with multiple rows per index/column pair.

# Re-Indexing & Altering Labels

6. **What is re-indexing in Pandas, and why is it used?**Re-indexing is the process of conforming a DataFrame to a new index, used to align data, fill missing values, or reorder rows/columns for consistency.
7. **Explain how to change the index and column labels of a DataFrame.**Use `df.index = new_index` to change the index and `df.columns = new_columns` to update column labels, where `new_index` and `new_columns` are lists or arrays.
8. **How can you reset the index of a DataFrame?**Use `df.reset_index(drop=True)` to reset the index to a default integer sequence, optionally dropping the old index.
9. **What happens if the new index values do not match the original DataFrame during reindexing?**Missing values are filled with `NaN` unless a `fill_value` is specified, and extra indices are ignored unless data is added.
10. **How do you rename specific rows or columns in a DataFrame?**
    Use `df.rename(index={'old_name': 'new_name'}, columns={'old_name': 'new_name'})` to rename specific rows or columns.

# Groupby() & Transform()

11. **What is the purpose of the groupby() function in Pandas?**The `groupby()` function groups data based on one or more columns, enabling split-apply-combine operations like aggregation or transformation.
12. **How is transform() different from aggregate() when used with groupby()?**`transform()` applies a function to each group and returns a DataFrame with the same shape, while `aggregate()` reduces the data to a single value per group.
13. **Explain a use case where transform() would be preferable over aggregate().**Use `transform()` to normalize values within groups (e.g., subtracting the group mean) while preserving the original DataFrame shape, unlike `aggregate()` which summarizes.
14. **How can you apply multiple aggregation functions to a grouped DataFrame?**Use `df.groupby('column').agg({'col1': ['sum', 'mean'], 'col2': 'max'})` to apply multiple functions to different columns.
15. **Write a small example where you group data by a column and then transform it to normalize values within each group.**

```python
import pandas as pd
df = pd.DataFrame({'Group': ['A', 'A', 'B', 'B'],
                   'Value': [10, 20, 30, 40]})
df['Normalized'] = df.groupby('Group')['Value'].transform(lambda x: (x - x.mean()) / x.std())
```

This normalizes `Value` within each `Group` using z-scores.
