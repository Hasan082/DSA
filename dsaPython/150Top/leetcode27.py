def removeElement(nums, val):
    count = 0
    for num in nums:
        if num != val:
            nums[count] = num
            count += 1
    return count


nums1 = [3, 2, 2, 3]
val1 = 3
print(removeElement(nums1, val1))  # output [2, 2]
