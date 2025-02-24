from typing import List
def decode(encoded: List[int], first: int) -> List[int]:
    arr = [first]
    for num in encoded:
        arr.append(arr[-1] ^ num)
    return arr


encoded1 = [1,2,3]
first1 = 1
print(decode(encoded1, first1)) # [1,0,2,3]
encoded2 = [6,2,7,3]
first2 = 4
print(decode(encoded2, first2)) # [4,2,0,7,4]