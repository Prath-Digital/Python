# Matplotlib: Chart Creation

## 1. What is Matplotlib, and why is it widely used for data visualization in Python?
Matplotlib is a popular plotting library in Python used for creating static, animated, and interactive visualizations. It is widely used due to its versatility, extensive customization options, and ability to produce publication-quality figures.

## 2. Which function is commonly used to create basic plots in Matplotlib?
The `plot()` function is commonly used to create basic plots in Matplotlib.

## 3. How can you create a simple bar chart using Matplotlib?
You can create a simple bar chart using the `bar()` function. Example: `plt.bar(categories, values)`.

## 4. What parameters can you set to customize a bar chart (like color, width, alignment)?
Parameters like `color` (to set bar color), `width` (to set bar width), and `align` (to set alignment, e.g., 'center' or 'edge') can be used to customize a bar chart.

## 5. Explain the basic structure of a line plot using Matplotlib.
A basic line plot involves importing Matplotlib (`import matplotlib.pyplot as plt`), preparing data (x and y values), and using `plt.plot(x, y)` followed by `plt.show()` to display the plot.

## 6. How can you add markers and change line styles in a line plot?
You can add markers with the `marker` parameter (e.g., `marker='o'`) and change line styles with the `linestyle` parameter (e.g., `linestyle='--'`) in the `plot()` function.

## 7. What is a scatter plot, and when would you prefer it over a line plot?
A scatter plot displays individual data points using dots, useful for showing relationships or distributions. Prefer it over a line plot when data is not sequential or to identify clusters/outliers.

## 8. Which Matplotlib function is used to create scatter plots?
The `scatter()` function is used to create scatter plots in Matplotlib.

## 9. How do you create a pie chart using Matplotlib, and what are key parameters like explode and autopct?
Create a pie chart with `plt.pie(values, labels=labels)`. Key parameters include `explode` (to offset slices) and `autopct` (to display percentage, e.g., `autopct='%1.1f%%'`).

## 10. What is the main purpose of a histogram, and how is it different from a bar chart?
The main purpose of a histogram is to show the distribution of a single variable by grouping data into bins. It differs from a bar chart, which compares distinct categories.

## 11. How do you control the number of bins in a histogram?
You can control the number of bins using the `bins` parameter in the `hist()` function (e.g., `plt.hist(data, bins=10)`).

## 12. What functions in Matplotlib help to add titles, labels, and legends to a plot?
Use `plt.title()` for titles, `plt.xlabel()` and `plt.ylabel()` for labels, and `plt.legend()` for legends.