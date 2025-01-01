from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        hIndex = len(citations)
        for citation in citations:
            if citation < hIndex:
                hIndex -= 1
            elif citation == hIndex:
                break
        return hIndex


print(Solution().hIndex([3, 0, 6, 1, 5]))
print(Solution().hIndex([1, 3, 1]))
print(Solution().hIndex([100]))
print(Solution().hIndex([0]))
print(Solution().hIndex([0, 1]))
