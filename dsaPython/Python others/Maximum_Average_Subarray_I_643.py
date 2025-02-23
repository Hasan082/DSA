from typing import List
def findMaxAverage(nums: List[int], k: int) -> float:
    first_sum = sum(nums[:k])
    avg = first_sum
    for i in range(k, len(nums)):
        first_sum += nums[i] - nums[i - k]
        avg = max(avg, first_sum)

    return avg / k



nums1 = [0,1,1,3,3]
k1 = 4
print(findMaxAverage(nums1, k1)) # 2.0
nums2 = [1,12,-5,-6,50,3]
k2 = 4
print(findMaxAverage(nums2, k2)) # 12.75
nums3 = [5]
k3 = 1
print(findMaxAverage(nums3, k3)) # 5.0
