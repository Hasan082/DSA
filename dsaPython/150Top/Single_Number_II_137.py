from typing import List
from collections import Counter


def singleNumber(self, nums: List[int]) -> int:
    ones, twos, threes = 0, 0, 0
    for num in nums:
        twos |= ones & num
        ones ^= num
        threes = ones & twos
        ones &= ~threes
        twos &= ~ threes
    return ones


nums1 = [2, 2, 3, 2]
nums2 = [0, 1, 0, 1, 0, 1, 99]

print(singleNumber(nums1))
print(singleNumber(nums2))
