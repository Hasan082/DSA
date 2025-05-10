# https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1?page=2&company=Amazon&sortBy=submissions

def findUnion(self,a,b):
    return sorted(set(a) | set(b))