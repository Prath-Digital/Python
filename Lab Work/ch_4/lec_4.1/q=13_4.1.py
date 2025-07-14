def fibonacci_sequence(n):
    """
    Generate a Fibonacci sequence up to a given number.
    
    This function calculates the Fibonacci sequence where each number is the sum of the
    two preceding ones, starting from 0 and 1. It returns a list containing the sequence
    up to (but not exceeding) the input number n.
    
    Args:
        n (int): The upper limit up to which the Fibonacci sequence should be generated.
                 Must be a non-negative integer.
    
    Returns:
        list: A list of integers representing the Fibonacci sequence up to n.
              Returns an empty list if n is less than 0.
    
    Example:
        >>> fibonacci_sequence(10)
        [0, 1, 1, 2, 3, 5, 8]
        >>> fibonacci_sequence(0)
        [0]
    """
    if n < 0:
        return []
    fib_seq = [0]
    if n == 0:
        return fib_seq
    a, b = 0, 1
    while b <= n:
        fib_seq.append(b)
        a, b = b, a + b
    return fib_seq

# Test the function
limit = int(input("Enter the upper limit for Fibonacci sequence: "))
result = fibonacci_sequence(limit)
print(f"Fibonacci sequence up to {limit}: {result}")