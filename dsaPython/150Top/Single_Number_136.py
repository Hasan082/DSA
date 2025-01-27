from typing import List


def singleNumber(nums: List[int]) -> int:
    res = 0
    for num in nums:
        res ^= num
    return res

nums1 = [2,2,1]
nums2 = [4,1,2,1,2]
print(singleNumber(nums1)) # 1
print(singleNumber(nums2)) # 4