def twoSum(nums: list[int], target: int) -> list[int]:
    maps = {}
    for i in range(len(nums)):
        secondNum = target - nums[i]
        if secondNum in maps:
            return [maps[secondNum], i]
        maps[nums[i]] = i


print(twoSum([2, 7, 11, 15], 9))  # Output: [0,1]
