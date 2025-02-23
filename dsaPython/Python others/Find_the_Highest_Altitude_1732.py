from typing import List
def largestAltitude(gain: List[int]) -> int:
    max_alt = 0
    current = 0
    for g in gain:
        current += g
        max_alt = max(max_alt, current)
    return max_alt


gain1 = [-5,1,5,0,-7]
print(largestAltitude(gain1)) # 1
gain2 = [-4,-3,-2,-1,4,3,2]
print(largestAltitude(gain2)) # 0