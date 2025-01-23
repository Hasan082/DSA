from typing import List


def plusOne(digits: list[int]) -> list[int]:
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

digits = [1, 2, 3]
digits2 = digits = [4, 3, 2, 1]
print(plusOne(digits))
print(plusOne(digits2))
