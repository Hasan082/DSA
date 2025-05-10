# https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1?page=1&company=Amazon&sortBy=submissions

def subarraySum(arr, target):
    start = 0
    curr_sum = 0
    for end in range(len(arr)):
        curr_sum += arr[end]
        while curr_sum > target and start <= end:
            curr_sum -= arr[start]
            start += 1
            
        if curr_sum == target:
            return [start+1, end+1]
            
    return [-1]
arr = [1, 2, 3, 7, 5]
target = 12
print(subarraySum(arr, target))

arr2 =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target2 = 15
print(subarraySum(arr2, target2))

arr3 = [5, 3, 4]
target3 = 2
print(subarraySum(arr3, target3))