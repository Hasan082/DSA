# https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1?page=2&company=Amazon&sortBy=submissions

def findFloor(arr, x):
    low, high = 0, len(arr) - 1
    indices  = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == x:
            indices = mid
            low = mid + 1
        elif arr[mid] < x:
            indices = mid
            low = mid + 1
        else:
            high = mid - 1
            
        
    return indices