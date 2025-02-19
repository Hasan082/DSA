from typing import List
def canAliceWin(nums: List[int]) -> bool:
    single_digit, double_digit = 0, 0
    for num in nums:
        if num < 10:
            single_digit += num
        else:
            double_digit += num
    return single_digit != double_digit



nums1 = [1,2,3,4,10]
nums2 = [1,2,3,4,5,14]
print(canAliceWin(nums1)) # False
print(canAliceWin(nums2)) # True