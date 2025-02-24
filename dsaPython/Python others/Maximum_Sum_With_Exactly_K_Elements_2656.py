from typing import List
def maximizeSum(nums: List[int], k: int) -> int:
    max_num = max(nums)
    res = 0
    for _ in range(k):
        res += max_num
        max_num += 1
    return res

