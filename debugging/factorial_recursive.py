#!/usr/bin/python3
import sys

def factorial(n):
    """
    Recursively calculates the factorial of a given non-negative integer.

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read the integer input from command-line arguments
f = factorial(int(sys.argv[1]))

# Print the result
print(f)