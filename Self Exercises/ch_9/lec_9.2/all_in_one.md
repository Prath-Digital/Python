# Stack Plot, Legends, Subplot, and Saving Charts

## 1. What is a stack plot, and how is it different from a regular line plot in Matplotlib?
A stack plot is a type of plot that displays the cumulative total of data series stacked on top of one another, often used to show the composition of a total over time. Unlike a regular line plot, which shows individual data series independently, a stack plot emphasizes the contribution of each series to the whole.

## 2. How do you create a stack plot in Matplotlib? What are the key parameters used for creating a stack plot?
You can create a stack plot using `plt.stackplot()`. Key parameters include `x` (x-axis values), `y` (list of datasets to stack), `labels` (for legend), and `colors` (to customize the appearance).

## 3. What is the purpose of a legend in a plot, and how can you add it using Matplotlib?
A legend helps identify the data series in a plot. You can add it using `plt.legend()` after plotting the data, passing labels defined earlier with the `label` parameter in plot functions.

## 4. How do you customize the position and appearance of the legend in Matplotlib?
You can customize the legend's position with `loc` (e.g., 'upper right') and appearance with parameters like `fontsize`, `frameon`, and `facecolor` in `plt.legend()`.

## 5. What is the purpose of a subplot in Matplotlib, and how do you create multiple subplots in a single figure?
A subplot divides a figure into multiple axes for displaying different plots. You can create multiple subplots using `plt.subplot()` or `plt.subplots()` with parameters like `nrows` and `ncols`.

## 6. Explain the role of plt.subplot() in Matplotlib. How does it help in creating multiple plots in one figure?
`plt.subplot()` creates a single subplot at a specified grid position (e.g., `plt.subplot(2, 1, 1)` for a 2x1 grid, first position). It helps organize multiple plots in one figure by defining their layout.

## 7. What is the difference between plt.subplot() and plt.subplots()?
`plt.subplot()` creates one subplot at a time, while `plt.subplots()` returns a figure and an array of axes for multiple subplots, making it easier to manage several plots together.

## 8. How can you customize each subplot (e.g., axis labels, titles) in Matplotlib?
You can customize each subplot by accessing its axes object (e.g., `ax`) and using methods like `ax.set_title()`, `ax.set_xlabel()`, and `ax.set_ylabel()`.

## 9. What function is used to save a plot as an image file (such as PNG, JPG, or PDF) in Matplotlib?
The `plt.savefig()` function is used to save a plot to an image file.

## 10. How can you control the resolution of the saved plot in Matplotlib?
You can control the resolution using the `dpi` parameter in `plt.savefig()` (e.g., `plt.savefig('plot.png', dpi=300)`).

## 11. Explain how to save a chart in Matplotlib in different formats (e.g., PNG, SVG, PDF).
Use `plt.savefig()` with the desired file extension (e.g., `plt.savefig('plot.png')` for PNG, `plt.savefig('plot.svg')` for SVG, `plt.savefig('plot.pdf')` for PDF) to save in different formats.

## 12. What is the role of dpi in saving a figure, and how does it affect the quality of the image file?
DPI (dots per inch) determines the resolution of the saved image. Higher DPI values result in sharper, higher-quality images but increase file size.