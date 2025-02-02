from typing import List
import itertools


def permute(nums: List[int]) -> List[List[int]]:
    return list(itertools.permutations(nums))


nums1 = [1, 2, 3]
nums2 = [0, 1]
print(permute(nums1))
print(permute(nums2))
