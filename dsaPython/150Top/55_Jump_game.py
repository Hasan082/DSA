from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        ln = len(nums)
        for i in range(ln):
            if i > farthest:
                return False

            if i + nums[i] > farthest:
                farthest = i + nums[i]

            if farthest >= ln - 1:
                return True


nums1 = [2, 3, 1, 1, 4]
nums2 = [3, 2, 1, 0, 4]
nums3 = [2,0]
nums4 = [0,1]
nums5 = [0]
nums6 = [1, 2, 3]
nums7 = [3, 2, 1]

result = Solution()
print(result.canJump(nums1))  # True
print(result.canJump(nums2))  # False
print(result.canJump(nums3))  # True
print(result.canJump(nums4))  # False
print(result.canJump(nums5))  # True
print(result.canJump(nums6))  # True
print(result.canJump(nums7))  # True
