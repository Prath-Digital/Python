# Read and Write CSV, JSON, and Excel files

## 1. What are the functions used in Pandas to read and write CSV files?

- **Read:** `pd.read_csv()`
- **Write:** `to_csv()`

## 2. How can you read a JSON file and write data to a JSON file using Pandas?

- **Read:** `pd.read_json()`
- **Write:** `to_json()`

## 3. What are some parameters of `read_csv()` and `read_excel()` functions, and how do they help in reading files?

- `sep`: Specifies the delimiter (e.g., ',' for CSV).
- `encoding`: Handles file encoding (e.g., 'utf-8').
- `skiprows`: Skips specified rows.
- These parameters help customize file reading based on structure and encoding.

## 4. How would you handle file paths and encoding issues when working with different file types in Pandas?

- Use absolute or relative paths with `os.path` for robustness.
- Specify `encoding='utf-8'` or other encodings (e.g., 'latin1') to avoid decoding errors.
- Test file reading with small samples to debug path/encoding issues.

# Handle missing values, duplicates, and data types

## 5. What is the purpose of `isnull()` and `dropna()` functions in Pandas?

- `isnull()`: Identifies missing (NaN) values.
- `dropna()`: Removes rows/columns with missing values.

## 6. How do you fill missing values using `fillna()` and what are the common strategies for filling them?

- Use `fillna(value)` (e.g., `fillna(0)` or `fillna(method='ffill')`).
- **Strategies:** Fill with mean, median, forward fill, backward fill, or a constant.

## 7. What is the difference between `drop_duplicates()` and `duplicated()` methods?

- `drop_duplicates()`: Removes duplicate rows.
- `duplicated()`: Returns a boolean series indicating duplicate rows.

## 8. How can you convert the data type of a column in a DataFrame using `astype()`?

- Example: `df['column'] = df['column'].astype('int')` converts to integer type.

# Handle dates and times using Pandas

## 9. What function is used to convert a column to datetime format in Pandas?

- Use `pd.to_datetime()`.

## 10. How can you extract the year, month, and day from a datetime object in a DataFrame?

- Example: `df['year'] = df['date'].dt.year`.

## 11. How do you perform date-based filtering in Pandas?

- Example: `df[df['date'].dt.year == 2023]` filters rows for 2023.

## 12. What are the common issues encountered when working with date and time data, and how can you handle them?

- **Issues:** Incorrect formats, missing values, timezone mismatches.
- **Handling:** Use `pd.to_datetime()` with `errors='coerce'` for invalid dates, set `dayfirst=True` for DD/MM/YYYY, and use `tz_localize()` for timezones.
