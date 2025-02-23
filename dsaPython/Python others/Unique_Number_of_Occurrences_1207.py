from collections import Counter
from typing import List 
def uniqueOccurrences(arr: List[int]) -> bool:
    count = Counter(arr)
    s = set()
    for val in count.values():
        s.add(val) 
    return len(s) == len(count.values())

arr1 = [1,2,2,1,1,3]
print(uniqueOccurrences(arr1)) # True
arr2 = [1,2]
print(uniqueOccurrences(arr2)) # False
arr3 = [-3,0,1,-3,1,1,1,-3,10,0]
print(uniqueOccurrences(arr3)) # True