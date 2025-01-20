from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    dic = {}
    for i in range(len(nums)):
        sec = target - nums[i]
        if sec in dic:
            return [dic[sec], i]
        else:
            dic[nums[i]] = i
