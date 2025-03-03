from math import factorial
from typing import List

def helper(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def generate(numRows: int) -> List[List[int]]:
    res = [] 
    for n in range(numRows):
        temp = []
        for k in range(n + 1):
            temp.append(helper(n, k))
        res.append(temp)
    return res


numRows1 = 5
print(generate(numRows1)) # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
numRows2 = 1
print(generate(numRows2)) # [[1]]
numRows3 = 2
print(generate(numRows3)) # [[1],[1,1]]
numRows4 = 3
print(generate(numRows4)) # [[1],[1,1],[1,2,1]]