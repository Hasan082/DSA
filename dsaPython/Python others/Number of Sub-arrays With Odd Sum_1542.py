from typing import List
def numOfSubarrays(arr: List[int]) -> int:
    curr_sum, odd = 0, 0
    even = 1
    for num in arr:
        curr_sum += num
        if curr_sum % 2 == 1:
            odd += 1
        else:
            even += 1
    return (odd * even) % (pow(10, 9) + 7)
