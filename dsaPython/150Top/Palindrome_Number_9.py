def isPalindrome(self, x: int) -> bool:
    s = str(x)
    if s == s[::-1]:
        return True
    else:
        return False


x1 = 121
x2 = -121
x3 = 10
print(isPalindrome(x1))
print(isPalindrome(x2))
print(isPalindrome(x3))
