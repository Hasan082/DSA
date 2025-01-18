from typing import List


class Solution:
    def maxArea(self, h: List[int]) -> int:
        ar = 0
        l, r = 0, len(h) - 1
        while l < r:
            if h[l] < h[r]:
                a = (r - l) * h[l]
                ar = max(a, ar)
                l += 1
            else:
                a = (r - l) * h[r]
                ar = max(a, ar)
                r -= 1

        return ar


s = Solution()

print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
print(s.maxArea([1, 1]))  # 1
