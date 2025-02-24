from typing import List
def minimumAverage(nums: List[int]) -> float:
    min_avg = float('inf')
    nums.sort()
    for i in range(len(nums) // 2):
        min_avg = min(min_avg, nums[i] + nums[-i - 1])
    return min_avg / 2


nums1 = [7,8,3,4,15,13,4,1]
print(minimumAverage(nums1)) # 5.5
nums2 = [1,9,8,3,10,5]
print(minimumAverage(nums2)) # 5.5