#!/usr/bin/python3
import sys

def factorial(n):
    """"
	Calculate the factorial of a given number.
	This function uses recursion to compute the factorial of n.
	The factorial of n is the product of all positive integers
	less than or equal to n.

	Parameters:
	n (int): The number for which to calculate the factorial.
				Must be a non-negative integer.

	Returns:
	int: The factorial of n.
	"""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
