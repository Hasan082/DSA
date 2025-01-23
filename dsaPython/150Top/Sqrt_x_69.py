def mySqrt(x: int) -> int:
    left, right = 0, x

    while left < right:
        mid = (left + right + 1) // 2
        if mid * mid > x:
            right = mid - 1
        else:
            left = mid

    return left


x1 = 4
x2 = 8
print(mySqrt(x1))
print(mySqrt(x2))
