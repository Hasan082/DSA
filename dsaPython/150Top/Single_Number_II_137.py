from typing import List
from collections import Counter


def singleNumber(nums: List[int]) -> int:
    counter = Counter(nums)
    res = 0
    for key, val in counter.items():
        if val == 1:
            res ^= key
    return res


nums1 = [2, 2, 3, 2]
nums2 = [0, 1, 0, 1, 0, 1, 99]

print(singleNumber(nums1))
print(singleNumber(nums2))
