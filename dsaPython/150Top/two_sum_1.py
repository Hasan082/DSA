from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    dic = {}
    for i in range(len(nums)):
        sec = target - nums[i]
        if sec in dic:
            return [dic[sec], i]
        else:
            dic[nums[i]] = i


nums1 = [2, 7, 11, 15]
target1 = 9
nums2 = [3, 2, 4]
target2 = 6

print(twoSum(nums1, target1))
print(twoSum(nums2, target2))
