from typing import List
def findNumbers(nums: List[int]) -> int:
    return sum(1 for num in nums if len(str(num)) % 2 == 0)


nums1 = [12,345,2,6,7896]
print(findNumbers(nums1)) # 2
nums2 = [555,901,482,1771]
print(findNumbers(nums2)) # 1