def check(nums):
    count = 0
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            count += 1

    if nums[0] < nums[len(nums) - 1]:
        count += 1
    return count < 2


print(check([3, 4, 5, 1, 2]))  # True
print(check([2, 1, 3, 4]))  # False
print(check([1, 2, 3]))  # True
