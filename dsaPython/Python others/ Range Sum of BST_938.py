from typing import Optional
class TreeNode:
    def __init__(self, val = 0, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBst(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        res = 0
        stack = [root]

        while stack:
            node = stack.pop()

            if low <=node.val <= high:
                res += node.val

            if node.right and node.val < high:
                stack.append(node.right)

            if node.left and node.val > low:
                stack.append(node.left)

        return res
    
root = [10, 5, 15, 3, 7, None, 18]
low = 7
high = 15
solution = Solution()

print(solution.rangeSumBst(root, low, high))
        
