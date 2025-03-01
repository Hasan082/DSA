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

# Time complexity: O(n)
# Space complexity: O(1)

# Test case
nums = [1,2,2,1,1,0]
print(applyOperations(nums)) # [2, 2, 2, 0, 0, 0]
nums = [0,1]
print(applyOperations(nums)) # [1, 0]