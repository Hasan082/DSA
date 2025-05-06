from typing import List


def search(nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
              return -1