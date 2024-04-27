def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    if k > n:
        k = k % n
    nums1 = nums[n - k:] + nums[:n - k]
    for i in range(len(nums1)):
        nums[i] = nums1[i]
    print(nums)


rotate([1, 2, 3, 4, 5, 6, 7], 3)  # output [5, 6, 7, 1, 2, 3, 4]
rotate([-1, -100, 3, 99], 2)  # output 3, 99, -1, -100]
