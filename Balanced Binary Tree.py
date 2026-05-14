from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        def dfs(node):
            if not node: return [True , 0]
            
            left_bal , left_height = dfs(node.left)
            right_bal , right_height = dfs(node.right)
          
            return ( left_bal and right_bal and abs( left_height - right_height ) <= 1 , 1 + max(left_height, right_height) )

        return dfs(root)[0]
        


def test_isBalanced():
    sol = Solution()

    # Test 1: Balanced tree
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert sol.isBalanced(root) == True

    # Test 2: Unbalanced tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)
    assert sol.isBalanced(root) == False

    # Test 3: Empty tree
    assert sol.isBalanced(None) == True

    # Test 4: Single node
    assert sol.isBalanced(TreeNode(1)) == True

    # Test 5: Skewed right
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    assert sol.isBalanced(root) == False

    print("All tests passed!")

test_isBalanced()