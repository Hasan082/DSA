def removeDuplicates(nums):
    if len(nums) <=2:
        return len(nums)

        slow = 2

    for fast in range(2, len(nums)):
        if nums[slow] != nums[fast-2]:
            nums[slow] = nums[fast]
            slow += 1

    return slow

