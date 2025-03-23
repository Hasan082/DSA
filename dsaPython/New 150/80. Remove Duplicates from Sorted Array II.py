def removeDuplicates(nums: list[int]) -> int:
    if len(nums) <= 2:
        return len(nums)

    i = 2

    for num in nums[2:]:
        if num != nums[i - 2]:
            nums[i] = num
            i += 1

    return i


nums1 = [1, 1, 1, 2, 2, 3]
print(removeDuplicates(nums1))
