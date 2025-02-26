from math import factorial
from typing import List
def helper(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))
def getRow(rowIndex: int) -> List[int]:
    res = [] 
    for n in range(rowIndex + 1):
        temp = []
        for k in range(n + 1):
            temp.append(helper(n, k))
        res.append(temp)
    return res[-1]

rowIndex = 3
print(getRow(rowIndex)) # [1,3,3,1]
rowIndex = 0
print(getRow(rowIndex)) # [1]
rowIndex = 1
print(getRow(rowIndex)) # [1,1]