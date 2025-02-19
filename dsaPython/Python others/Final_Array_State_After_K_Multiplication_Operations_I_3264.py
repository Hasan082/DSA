from typing import List
def getFinalState(nums: List[int], k: int, multiplier: int) -> List[int]:
    for i in range(k):
        nums[nums.index(min(nums))] = min(nums) * multiplier
    return nums

