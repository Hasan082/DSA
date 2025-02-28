def factorial_1(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial_2(n):
    if n == 0:
        return 1
    for i in range(1, n):
        n *= i
    return n


from math import factorial
def factorial_3(n):
    return factorial(n)

num = int(input("Enter a number: "))
print(f"The factorial fn_1 of {num} is {factorial_1(num)}")
print(f"The factorial fn_2 of {num} is {factorial_2(num)}")
print(f"The factorial fn_3 of {num} is {factorial_3(num)}")
