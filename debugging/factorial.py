#!/usr/bin/python3
import sys

def factorial(n):
    """
    calculate the factorial recursivly
    the factorial nums r from 1 to n
    with 0 an exception
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = int(sys.argv[1])

result = factorial(number)
print(result)