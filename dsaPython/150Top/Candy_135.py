from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for j in range(n - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                candies[j] = max(candies[j], candies[j + 1] + 1)

        return sum(candies)


res = Solution()

print(res.candy([1, 0, 2]))  # 5
print(res.candy([1, 2, 2]))  # 4
print(res.candy([1, 2, 87, 87, 87, 2, 1]))  # 13
