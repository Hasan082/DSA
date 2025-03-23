def removeDuplicates(nums: list[int]) -> int:
    count = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[count] = nums[i]
            count += 1

    return count


nums1 = [1, 1, 2]
print(removeDuplicates(nums1))
