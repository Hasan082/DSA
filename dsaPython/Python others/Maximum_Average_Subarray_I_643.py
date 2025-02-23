from typing import List
def findMaxAverage(nums: List[int], k: int) -> float:
    first_sum = sum(nums[:k])
    avg = first_sum
    for i in range(k, len(nums)):
        first_sum += nums[i] - nums[i - k]
        avg = max(avg, first_sum)

    return avg / k