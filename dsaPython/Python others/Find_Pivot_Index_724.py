from typing import List
def pivotIndex(nums: List[int]) -> int:
    left_sum, total_sum = 0, sum(nums)
    for i , num in enumerate(nums):
        if left_sum == (total_sum - left_sum - num): return i
        left_sum += num
    return -1

nums1 = [1,7,3,6,5,6]
print(pivotIndex(nums1)) # 3
nums2 = [1,2,3]
print(pivotIndex(nums2)) # -1