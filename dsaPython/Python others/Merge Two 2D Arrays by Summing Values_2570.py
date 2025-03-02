from typing import List
from collections import defaultdict

def mergeArrays(nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
    maps = defaultdict(int)
    arr = nums1 + nums2
     
    for num in arr:
        maps[num[0]] += num[1]

    return sorted(maps.items())


nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]
print( mergeArrays(nums1, nums2))