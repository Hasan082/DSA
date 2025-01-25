# Question 2
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


result = factorial(8)
print(result)