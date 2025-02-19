from typing import List
def getFinalState(nums: List[int], k: int, multiplier: int) -> List[int]:
    for i in range(k):
        nums[nums.index(min(nums))] = min(nums) * multiplier
    return nums

nums = [2, 1, 3, 5, 6]
k = 5
multiplier = 2

print(getFinalState(nums, k, multiplier)) # [8,4,6,5,6]