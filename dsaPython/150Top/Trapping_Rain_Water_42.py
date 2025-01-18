from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lm, rm = height[l], height[r]
        water = 0
        while l < r:
            if lm < rm:
                l += 1
                lm = max(lm, height[l])
                water += lm - height[l]
            else:
                r -= 1
                rm = max(rm, height[r])
                water += rm - height[r]

        return water


s = Solution()
print(s.trap([4, 2, 0, 3, 2, 5])) # 9
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])) # 6
