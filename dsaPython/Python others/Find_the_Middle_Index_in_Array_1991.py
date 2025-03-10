from typing import List
def findMiddleIndex(nums: List[int]) -> int:
    left_sum, total_sum = 0, sum(nums)
    for i , num in enumerate(nums):
        if left_sum == (total_sum - left_sum - num): return i
        left_sum += num
    return -1

nums1 = [2,3,-1,8,4]
print(findMiddleIndex(nums1)) # 3
nums2 = [1,-1,4]
print(findMiddleIndex(nums2)) # 2