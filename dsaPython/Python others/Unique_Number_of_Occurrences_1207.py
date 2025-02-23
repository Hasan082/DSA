from collections import Counter
from typing import List 
def uniqueOccurrences(arr: List[int]) -> bool:
    count = Counter(arr)
    s = set()
    for val in count.values():
        s.add(val) 
    return len(s) == len(count.values())