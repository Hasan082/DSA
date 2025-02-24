from typing import List
def decode(encoded: List[int], first: int) -> List[int]:
    arr = [first]
    for num in encoded:
        arr.append(arr[-1] ^ num)
    return arr