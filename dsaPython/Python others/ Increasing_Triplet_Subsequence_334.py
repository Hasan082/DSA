from typing import List
def increasingTriplet(nums: List[int]) -> bool:
    f = 2**31 - 1
    s = 2**31 - 1
    for n in nums:
        if n <= f:
            f = n
        elif n <= s:
            s = n
        else:
            return True
    return False