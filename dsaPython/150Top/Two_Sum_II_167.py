from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            cur_sum = numbers[left] + numbers[right]
            if cur_sum > target:
                right -= 1
            elif cur_sum < target:
                left += 1
            else:
                return [left + 1, right + 1]


numbers1 = [2, 7, 11, 15]
target1 = 9
numbers2 = [2, 3, 4]
target2 = 6
numbers3 = [-1, 0]
target3 = -1
sol = Solution()
print(sol.twoSum(numbers1, target1))
print(sol.twoSum(numbers2, target2))
print(sol.twoSum(numbers3, target3))
