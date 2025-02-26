from typing import List
from itertools import accumulate
def maxAbsoluteSum(nums: List[int]) -> int:    
    l = list(accumulate(nums, initial = 0))
    return max(l) - min(l)