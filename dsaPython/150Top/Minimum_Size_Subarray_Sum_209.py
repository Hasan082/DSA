from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_length = float('inf')
        left = 0
        current_sum = 0

        for right in range(n):
            current_sum += nums[right]
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        return min_length if min_length != float('inf') else 0


res = Solution()
print(res.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # 2
print(res.minSubArrayLen(4, [1, 4, 4]))  # 1
print(res.minSubArrayLen(11, [1, 2, 3, 4, 5]))  # 3
print(res.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))  # 0
