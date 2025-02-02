def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    return str(x) == str(x)[::-1]


x1 = 121
x2 = -121
x3 = 10
print(isPalindrome(x1))
print(isPalindrome(x2))
print(isPalindrome(x3))
