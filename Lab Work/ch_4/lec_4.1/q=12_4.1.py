def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    This function multiplies the length and width to compute the area of a rectangle.
    
    Args:
        length (float or int): The length of the rectangle.
        width (float or int): The width of the rectangle.
    
    Returns:
        float or int: The area of the rectangle.
    
    Example:
        >>> calculate_area(5, 3)
        15
    """
    return length * width

# Print the doc string
print(calculate_area.__doc__)

# Test the function
print(f"Area: {calculate_area(5, 3)}")