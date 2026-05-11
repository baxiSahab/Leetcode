from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        return 1+ max(self.maxDepth(root.left) , self.maxDepth(root.right))
        
# 1. Basic tree
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)
# Expected: 3

# 2. Single node
root2 = TreeNode(1)
# Expected: 1

# 3. Empty tree
root3 = None
# Expected: 0

# 4. Right-skewed tree
root4 = TreeNode(1)
root4.right = TreeNode(2)
root4.right.right = TreeNode(3)
# Expected: 3

# 5. Perfect binary tree (depth 4)
root5 = TreeNode(1)
root5.left = TreeNode(2)
root5.right = TreeNode(3)
root5.left.left = TreeNode(4)
root5.left.right = TreeNode(5)
root5.right.left = TreeNode(6)
root5.right.right = TreeNode(7)
root5.left.left.left = TreeNode(8)
# Expected: 4

s = Solution()
print(s.maxDepth(root1))  # 3
print(s.maxDepth(root2))  # 1
print(s.maxDepth(root3))  # 0
print(s.maxDepth(root4))  # 3
print(s.maxDepth(root5))  # 4