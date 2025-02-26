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


arr1 = [1,3,5]
print(numOfSubarrays(arr1)) # 4
arr2 = [2,4,6]
print(numOfSubarrays(arr2)) # 0
arr3 = [1,2,3,4,5,6,7]
print(numOfSubarrays(arr3)) # 16