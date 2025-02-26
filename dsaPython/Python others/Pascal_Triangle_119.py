from math import factorial
from typing import List
def helper(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))
def generate(self, numRows: int) -> List[List[int]]:
    res = [] 
    for n in range(numRows):
        temp = []
        for k in range(n + 1):
            temp.append(self.helper(n, k))
        res.append(temp)
    return res

