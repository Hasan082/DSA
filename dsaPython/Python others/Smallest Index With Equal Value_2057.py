from typing import List
def smallestEqual(nums: List[int]) -> int:
    ans = float("inf")
    mod = 10
    for i in range(len(nums)):
        total = i % mod
        if total == nums[i]:
            ans = min(ans, i)
    return ans if ans != float("inf") else -1


nums = [0,1,2]
print(smallestEqual(nums)) # Expected 0
nums = [4,3,2,1]
print(smallestEqual(nums)) # Expected 2