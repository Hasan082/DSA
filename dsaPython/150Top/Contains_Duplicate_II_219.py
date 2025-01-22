from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    d = {}
    if len(set(nums)) == len(nums):
        return False
    for i, n in enumerate(nums):
        if n in d and abs(i - d[n]) <= k:
            return True
        d[n] = i

    return False
