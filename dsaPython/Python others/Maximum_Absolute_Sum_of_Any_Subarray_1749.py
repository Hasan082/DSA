from typing import List
from itertools import accumulate
def maxAbsoluteSum(nums: List[int]) -> int:    
    l = list(accumulate(nums, initial = 0))
    return max(l) - min(l)

nums1 = [1,-3,2,3,-4]
print(maxAbsoluteSum(nums1)) # 5
nums2 = [2,-5,1,-4,3,-2]
print(maxAbsoluteSum(nums2)) # 8
nums3 = [1,2,3]
print(maxAbsoluteSum(nums3)) # 6