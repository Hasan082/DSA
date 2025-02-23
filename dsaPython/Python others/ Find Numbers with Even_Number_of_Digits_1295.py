from typing import List
def findNumbers(nums: List[int]) -> int:
    return sum(1 for num in nums if len(str(num)) % 2 == 0)