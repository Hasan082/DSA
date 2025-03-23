def majorityElement(nums: list[int]) -> int:
    nums.sort()
    return nums[len(nums) // 2]


nums = [3, 2, 3]
print(majorityElement(nums))


# ALTERNATIVE APPROACH
# from collections import Counter
# def majorityElement(nums: List[int]) -> int:
#     count = Counter(nums)
#     max_num = max(count.values())
#     for key, val in count.items():
#         if val == max_num:
#             return key
