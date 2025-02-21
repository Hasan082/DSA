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

nums1 = [1,2,3,4,5]
print(increasingTriplet(nums1)) # True
nums2 = [5,4,3,2,1]
print(increasingTriplet(nums2)) # False
nums3 = [2,1,5,0,4,6]
print(increasingTriplet(nums3)) # True
nums4 = [20,100,10,12,5,13]
print(increasingTriplet(nums4)) # True
nums5 = [1,1,1,1,1]
print(increasingTriplet(nums5)) # False