from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, total_gas, total_cost, current = 0, sum(gas), sum(cost), 0

        if total_gas < total_cost:
            return -1

        for i in range(len(gas)):
            current += gas[i] - cost[i]
            if current < 0:
                current = 0
                start = i + 1

        return start


res = Solution().canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2])

print(res)
