from typing import List
def maxSubsequence(nums: List[int], k: int) -> List[int]:
    sorted_index = sorted([(num, i) for i, num in enumerate(nums)])
    top_k = sorted_index[-k:]
    top_k_sorted = sorted(top_k, key=lambda x:x[1])
    return [x[0] for x in top_k_sorted]


nums = [2, 1, 3, 3]
k = 2
print(maxSubsequence(nums, k)) # Expected [3, 3]
nums = [-1,-2,3,4]
k = 3
print(maxSubsequence(nums, k)) # Expected [-1,3,4]