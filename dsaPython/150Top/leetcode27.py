def removeElement(nums, val):
    count = nums.count(val)
    # count = 0
    # for i in range(len(nums)):
    #     if nums[i] != val:
    #         nums[count] = nums[i]
    #         count += 1
    return nums.count(val)


nums1 = [3, 2, 2, 3]
val1 = 3
print(removeElement(nums1, val1))  # output [2, 2]
