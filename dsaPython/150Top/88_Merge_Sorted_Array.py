from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(m, len(nums1)):
            nums1[i] = nums2[i - m]

        nums1.sort()
        print(nums1)


numsArr1 = [1, 2, 3, 0, 0, 0]
m1 = 3
numsArr2 = [2, 5, 6]
n1 = 3

result = Solution()
result.merge(numsArr1, m1, numsArr2, n1)
