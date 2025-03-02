from collections import Counter
from typing import List
def frequencySort(nums: List[int]) -> List[int]:
    count = Counter(nums)
    return sorted(nums, key=lambda x: (count[x], -x))