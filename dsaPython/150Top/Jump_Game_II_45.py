from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> int:
        far, count, ln, end = 0, 0, len(nums), 0
        if ln <= 1:
            return 0
        for i in range(0, len(nums)):
            far = max(far, i + nums[i])

            if i == end:
                count += 1
                end = far

            if far >= ln - 1:
                break

        return count


result = Solution()
nums1 = [2, 3, 1, 1, 4]
nums2 = [2, 3, 0, 1, 4]
nums3 = [0]

print(result.canJump(nums1))  # Ans: 2
print(result.canJump(nums2))  # Ans: 2
print(result.canJump(nums3))  # Ans: 0
