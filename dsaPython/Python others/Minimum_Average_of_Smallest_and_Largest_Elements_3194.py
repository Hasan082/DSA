from typing import List
def minimumAverage(nums: List[int]) -> float:
    min_avg = float('inf')
    nums.sort()
    for i in range(len(nums) // 2):
        min_avg = min(min_avg, nums[i] + nums[-i - 1])
    return min_avg / 2