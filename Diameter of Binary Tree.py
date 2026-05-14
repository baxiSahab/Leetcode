class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = 0
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.res = max(self.res , left + right)
            return 1 + max(left , right)
        
        dfs(root)
        return self.res
    
        
     
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_level_order(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

s = Solution()

t1 = build_tree_level_order([1, 2, 3, 4, 5])
print(s.diameterOfBinaryTree(t1))  # Expected: 3

t2 = build_tree_level_order([1, None, 2, None, 3])
print(s.diameterOfBinaryTree(t2))  # Expected: 2

t3 = build_tree_level_order([1])
print(s.diameterOfBinaryTree(t3))  # Expected: 0

t4 = build_tree_level_order([1, None, 2])
print(s.diameterOfBinaryTree(t4))  # Expected: 1

# Test 5 needs manual build (left-skewed with specific shape)
t5 = TreeNode(1)
t5.left = TreeNode(2)
t5.left.left = TreeNode(3)
t5.left.right = TreeNode(4)
t5.left.left.left = TreeNode(5)
print(s.diameterOfBinaryTree(t5))  # Expected: 3