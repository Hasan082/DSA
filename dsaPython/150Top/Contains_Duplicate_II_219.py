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


nums1 = [1, 2, 3, 1]
k1 = 3

nums2 = [1, 0, 1, 1]
k2 = 1

nums3 = [1, 2, 3, 1, 2, 3]
k3 = 2

print(containsNearbyDuplicate(nums1, k1))  # True
print(containsNearbyDuplicate(nums2, k2))  # True
print(containsNearbyDuplicate(nums3, k3))  # False
