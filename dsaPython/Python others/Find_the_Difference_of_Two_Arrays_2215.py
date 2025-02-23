from typing import List
def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]


nums1 = [1,2,3]
nums2 = [2,4,6]
print(findDifference(nums1, nums2)) # [[5], []]
nums3 = [1,2,3,3]
nums4 = [1,1,2,2]
print(findDifference(nums3, nums4)) # [[3],[]]