from typing import List
def convert_num( digit):
    total = 0
    while digit > 0:
        total += digit % 10
        digit //= 10
    return total

def minElement(nums: List[int]) -> int:
    return min(convert_num(num) for num in nums)

nums = [10,12,13,14]

print(minElement(nums)) # 1