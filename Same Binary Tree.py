class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
     
        if not p and not q: return True
        if not p and q: return False
        if p and not q: return False
        pp = p.val
        qq = q.val

        # if pp and qq

        if pp == qq:
            return self.isSameTree(p.left , q.left) and self.isSameTree(p.right , q.right)
        
        else: return False
    

# Test 1: Identical trees
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
s = Solution()
print(s.isSameTree(p, q)) 
# Expected: True

# Test 2: Different values
p = TreeNode(1, TreeNode(2), None)
q = TreeNode(1, None, TreeNode(2))
s = Solution()
print(s.isSameTree(p, q)) 
# Expected: False

# Test 3: Both empty
p = None
q = None
s = Solution()
print(s.isSameTree(p, q)) 
# Expected: True

# Test 4: One empty, one not
p = TreeNode(1)
q = None
s = Solution()
print(s.isSameTree(p, q)) 
# Expected: False

# Test 5: Different values, same structure
p = TreeNode(1, TreeNode(2), TreeNode(1))
q = TreeNode(1, TreeNode(1), TreeNode(2))
s = Solution()
print(s.isSameTree(p, q)) 
# Expected: False
s = Solution()
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
print(s.isSameTree(p, q))  # Expected: True