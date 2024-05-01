def removeDuplicates(nums):
    count = 1
    for i in range(1, len(nums)):
        if count == 1 or nums[i] != nums[count - 2]:
            nums[count] = nums[i]
            count += 1
    return count
