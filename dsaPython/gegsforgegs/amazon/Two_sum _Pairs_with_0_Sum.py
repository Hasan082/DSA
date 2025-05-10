# https://www.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1?page=2&company=Amazon&sortBy=submissions

def getPairs(arr):
    res = []
    arr.sort()
    left, right = 0, len(arr) - 1
    while left < right:
        total = arr[left] + arr[right]
        if total == 0:
            res.append([arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif total < 0:
            left += 1
        else:
            right -= 1
            
    return res


print(getPairs([-1, 0, 1, 2, -1, -4]))