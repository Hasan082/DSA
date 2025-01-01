from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, total, current = 0, 0, 0
        for i in range(len(gas)):
            gas_gain = gas[i] - cost[i]
            total += gas_gain
            current += gas_gain
            if current >= 0:
                current = 0
                start = i + 1

        return -1 if total < 0 else start


res = Solution().canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2])

print(res)
