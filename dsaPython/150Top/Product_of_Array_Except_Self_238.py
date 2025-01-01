from math import prod
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        total, ln = prod(nums), len(nums)
        for num in nums:
            if num:
                res.append(total // num)
            else:
                prefix = nums[:len(res)]
                suffix = nums[len(res) + 1:]
                sub_total = prod(prefix + suffix)
                res.append(sub_total)
                if total == 0 and sub_total == 0: return [0] * ln

        return res


result = Solution()
nums1 = [1, 2, 3, 4]
nums2 = [-1, 1, 0, -3, 3]

print(result.productExceptSelf(nums1))
print(result.productExceptSelf(nums2))
