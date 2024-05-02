def findMaxK(nums):
    mySet = set(nums)
    res = -1
    for i in nums:
        if -i in mySet:
            res = max(res, i)
    return res


print(findMaxK([-37, 37, -9, 2, 47, 18, 13, -11, 9, -28]))
