# https://www.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1?page=1&company=Amazon&sortBy=submissions

def rotateArr(arr, d):
    for _ in range(d):
        d = d % len(arr)
    arr[:] = arr[d:] + arr[:d]
    return arr

print(rotateArr([1, 2, 3, 4, 5], 2))