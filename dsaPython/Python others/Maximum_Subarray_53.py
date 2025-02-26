from typing import List
def maxSubArray(nums: List[int]) -> int:
    max_sum = float('-inf')
    curr_sum=0
    for num in nums:
        curr_sum+=num
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum<0:
            curr_sum=0
    return max_sum

nums1 = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums1)) # 6
nums2 = [1]
print(maxSubArray(nums2)) # 1
nums3 = [5,4,-1,7,8]
print(maxSubArray(nums3)) # 23