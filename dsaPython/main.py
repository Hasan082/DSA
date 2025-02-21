from typing import List
def increasingTriplet(nums: List[int]) -> bool:
    first, second = float('inf'), float('inf')
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
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
nums6 = [1,1,3,1,1,1]
print(increasingTriplet(nums6)) # False

  









