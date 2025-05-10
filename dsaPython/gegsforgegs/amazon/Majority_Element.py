# https://www.geeksforgeeks.org/problems/majority-element-1587115620/1?page=1&company=Amazon&sortBy=submissions

def Majority_elements(arr):
    candidate = None
    count = 0
        
    for num in arr:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
        
    count = sum(1 for num in arr if num == candidate)
        
    if count > len(arr) // 2:
        return candidate
    else:
        return -1
    
print(Majority_elements([1, 1, 2, 1, 3, 5, 1]))
print(Majority_elements( [7]))
print(Majority_elements([2, 13]))