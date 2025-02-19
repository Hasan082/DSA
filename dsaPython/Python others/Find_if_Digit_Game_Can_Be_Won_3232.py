from typing import List
def canAliceWin(nums: List[int]) -> bool:
    single_digit, double_digit = 0, 0
    for num in nums:
        if num < 10:
            single_digit += num
        else:
            double_digit += num
    return single_digit != double_digit