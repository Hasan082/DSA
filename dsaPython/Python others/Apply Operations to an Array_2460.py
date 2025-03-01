from typing import List
def applyOperations(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(n - 1):
        if nums[i] == nums[i + 1]:
            nums[i], nums[i + 1] = nums[i] * 2, 0
    count_zero = 0
    for i in range(n):
        if nums[i] != 0:
            nums[count_zero] = nums[i]
            count_zero += 1
            
    for i in range(count_zero, n):
        nums[i] = 0
    
    return nums