from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])

        return profit


result = Solution()
prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [1, 2, 3, 4, 5]
prices3 = [7,6,4,3,1]
print(result.maxProfit(prices1)) # ans: 7
print(result.maxProfit(prices2)) # ans 4
print(result.maxProfit(prices3)) # ans 0
