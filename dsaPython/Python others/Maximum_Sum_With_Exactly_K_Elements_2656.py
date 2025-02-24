from typing import List
def maximizeSum(nums: List[int], k: int) -> int:
    max_num = max(nums)
    res = 0
    for _ in range(k):
        res += max_num
        max_num += 1
    return res

nums1 = [1,2,3,4,5]
k1 = 3
print(maximizeSum(nums1, k1)) # 18
nums2 = [5,5,5]
k2 = 2
print(maximizeSum(nums2, k2)) # 11