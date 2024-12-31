from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = float('inf')
        profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > profit:
                profit = price - min_price

        return profit


prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]
result = Solution()
print(result.maxProfit(prices1))  # Ans 5
print(result.maxProfit(prices2))  # Ans 0

