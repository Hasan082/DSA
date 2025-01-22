from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
    res, start = [], None
    for i, num in enumerate(nums):
        if start is None:
            start = num
        if i == len(nums) - 1 or nums[i + 1] != num + 1:
            res.append(f"{start}" if start == num else f"{start}->{num}")
            start = None
    return res



