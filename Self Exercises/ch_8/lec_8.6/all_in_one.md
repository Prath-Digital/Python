# Summarize and Visualize data: Sorting, Filtering & Aggregation

## Merging and Joining data using Pandas

1. **What are the different ways to summarize a DataFrame in Pandas?**  
   - You can summarize a DataFrame using methods like `describe()`, `info()`, `sum()`, `mean()`, `median()`, `min()`, `max()`, and `count()` to get statistical summaries or basic information.

2. **Explain the difference between `sort_values()` and `sort_index()` in Pandas.**  
   - `sort_values()` sorts the DataFrame by the values in one or more columns.  
   - `sort_index()` sorts the DataFrame by its index labels.

3. **How does filtering work in Pandas using Boolean indexing?**  
   - Filtering with Boolean indexing involves creating a Boolean Series (True/False values) based on a condition, then using it to select rows where the condition is True, e.g., `df[df['column'] > 10]`.

4. **Write a use-case for filtering data using multiple conditions in Pandas.**  
   - Use-case: Filter a sales DataFrame to find products with sales > 100 and profit > 50.  
     Example: `df[(df['sales'] > 100) & (df['profit'] > 50)]`.

5. **What is aggregation in Pandas? List some common aggregation functions.**  
   - Aggregation involves combining data into a single value, like calculating totals or averages. Common functions include `sum()`, `mean()`, `min()`, `max()`, `count()`, and `std()`.

6. **How does the `groupby()` function help in data analysis?**  
   - `groupby()` groups data based on a column or index, allowing aggregation operations (e.g., sum, mean) on each group to analyze subsets of data.

7. **What is the difference between `agg()` and `apply()` in Pandas?**  
   - `agg()` applies one or more aggregation functions to grouped data (e.g., `sum`, `mean`).  
   - `apply()` applies a custom function to each group or the entire DataFrame for more flexible operations.

8. **How can you create basic visualizations using Pandas built-in plotting features?**  
   - Use `df.plot()` to create line, bar, histogram, or scatter plots directly from a DataFrame, e.g., `df.plot(kind='bar')`.

9. **What is the role of the `plot()` function in visualizing Pandas data?**  
   - The `plot()` function provides a simple interface to generate various plots (line, bar, etc.) using Matplotlib, based on DataFrame or Series data.

10. **Describe the process of merging two DataFrames using the `merge()` function.**  
    - Use `merge()` to combine two DataFrames based on a common column or index, specifying the join type (e.g., inner, outer) and the key column with the `on` parameter.

11. **What are the different types of joins available in Pandas?**  
    - Types include inner, outer, left, and right joins, determining how rows from the DataFrames are combined based on the key.

12. **Explain the difference between `merge()`, `join()`, and `concat()` in Pandas.**  
    - `merge()` combines DataFrames on a common column.  
    - `join()` merges DataFrames based on their indexes.  
    - `concat()` stacks DataFrames vertically or horizontally without requiring a common key.

13. **How does the `on` parameter work in `merge()`? Give an example.**  
    - The `on` parameter specifies the column(s) to join on.  
      Example: `df1.merge(df2, on='id')` merges `df1` and `df2` using the 'id' column.

14. **How can you join DataFrames on index instead of columns?**  
    - Use `join()` with the default index-based merging, e.g., `df1.join(df2)`.

15. **What precautions should be taken while merging DataFrames with overlapping column names?**  
    - Use suffixes with the `suffixes` parameter (e.g., `suffixes=('_x', '_y')`) to distinguish overlapping columns, and check for unintended data loss.