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


nums1 = [0, 1, 2, 4, 5, 7]
print(summaryRanges(nums1))  # ["0->2","4->5","7"]
nums2 = [0, 2, 3, 4, 6, 8, 9]
print(summaryRanges(nums2))  # ["0","2->4","6","8->9"]
