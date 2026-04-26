# Definition for a binary tree node.
# this solution is fine but the serialized version best
class TreeNode:
    class Solution:
        def searialize(self, node):
            if not node:
                return 'N'
            return f"({node.val}, {self.searialize(node.left)}, {self.searialize(node.right)})"
        
      

        # def isSame(self, node1, node2):  # Add self here!
        #     if node1 is None and node2 is None:
        #         return True
        #     elif node1 is None or node2 is None:
        #         return False
        #     elif node1.val != node2.val:
        #         return False
        #     else:
        #         return self.isSame(node1.left, node2.left) and self.isSame(node1.right, node2.right)


        # def isSubtree(self, root: Optional[TreeNode], subRoot: # Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    """Convert tree to string representation"""
    if not node:
        return 'N'
    return f"({node.val}, {serialize(node.left)}, {serialize(node.right)})"


def isSubtree(root, subRoot):
    """
    Determine if subRoot is a subtree of root.
    
    Uses serialization approach:
    - Convert both trees to string representation
    - Check if subRoot's serialization is a substring of root's serialization
    """
    if root is None and subRoot is None:
        return True
    if root is None or subRoot is None:
        return False
    
    serial_root = serialize(root)
    serial_subroot = serialize(subRoot)
    
    return serial_subroot in serial_root


# ============================================
# TEST CASES
# ============================================

def run_tests():
    print("Running Subtree of Another Tree tests...\n")
    
    # Test 1: Basic case - subRoot is a subtree
    root1 = TreeNode(3)
    root1.left = TreeNode(4)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(2)
    
    subRoot1 = TreeNode(4)
    subRoot1.left = TreeNode(1)
    subRoot1.right = TreeNode(2)
    
    test1 = isSubtree(root1, subRoot1)
    print("Test 1 - Basic subtree match:")
    print("Expected: True")
    print(f"Got: {test1}")
    print(f"Status: {'✓ PASS' if test1 == True else '✗ FAIL'}")
    print()
    
    # Test 2: subRoot is not a subtree (different structure)
    root2 = TreeNode(3)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(2)
    
    subRoot2 = TreeNode(4)
    subRoot2.left = TreeNode(1)
    
    test2 = isSubtree(root2, subRoot2)
    print("Test 2 - Partial structure (not a subtree):")
    print("Expected: False")
    print(f"Got: {test2}")
    print(f"Status: {'✓ PASS' if test2 == False else '✗ FAIL'}")
    print()
    
    # Test 3: Single node - subRoot equals root
    root3 = TreeNode(1)
    subRoot3 = TreeNode(1)
    
    test3 = isSubtree(root3, subRoot3)
    print("Test 3 - Single node match:")
    print("Expected: True")
    print(f"Got: {test3}")
    print(f"Status: {'✓ PASS' if test3 == True else '✗ FAIL'}")
    print()
    
    # Test 4: subRoot is the entire root tree
    root4 = TreeNode(1)
    root4.left = TreeNode(1)
    
    subRoot4 = TreeNode(1)
    subRoot4.left = TreeNode(1)
    
    test4 = isSubtree(root4, subRoot4)
    print("Test 4 - Entire tree matches:")
    print("Expected: True")
    print(f"Got: {test4}")
    print(f"Status: {'✓ PASS' if test4 == True else '✗ FAIL'}")
    print()
    
    # Test 5: Duplicate values but different structure
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.left.left = TreeNode(3)
    
    subRoot5 = TreeNode(2)
    subRoot5.right = TreeNode(3)
    
    test5 = isSubtree(root5, subRoot5)
    print("Test 5 - Duplicate values, different structure:")
    print("Expected: False")
    print(f"Got: {test5}")
    print(f"Status: {'✓ PASS' if test5 == False else '✗ FAIL'}")
    print()
    
    # Test 6: Deep linear tree (like linked list)
    root6 = TreeNode(1)
    root6.right = TreeNode(1)
    root6.right.right = TreeNode(1)
    root6.right.right.right = TreeNode(2)
    
    subRoot6 = TreeNode(1)
    subRoot6.right = TreeNode(2)
    
    test6 = isSubtree(root6, subRoot6)
    print("Test 6 - Deep nested tree:")
    print("Expected: True")
    print(f"Got: {test6}")
    print(f"Status: {'✓ PASS' if test6 == True else '✗ FAIL'}")
    print()


# Run all tests
if __name__ == "__main__":
    run_tests(Optional[TreeNode]) -> bool:
        #     if root is None:
        #         return False
            
        #     return self.isSame(root, subRoot)  or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

# Your solution here
def isSubtree(root, subRoot):
    """
    Determine if subRoot is a subtree of root.
    
    Args:
        root: The main binary tree
        subRoot: The tree to check if it exists as a subtree
    
    Returns:
        bool: True if subRoot is a subtree of root, False otherwise
    
    Guidelines:
    - A subtree means the entire structure, values, and arrangement must match exactly
    - It's not just about having the same values somewhere in the tree
    """

    searialRoot = searialize(Root)
    serialSubroot = searialize(subRoot)

    return serialSubroot in searialRoot


    # TODO: Implement your solution
    # if root is None:
    #     return False
    
    # return isSame(root, subRoot)
    
    


# ============================================
# TEST CASES
# ============================================

def run_tests():
    print("Running Subtree of Another Tree tests...\n")
    
    # Test 1: Basic case - subRoot is a subtree
    root1 = TreeNode(3)
    root1.left = TreeNode(4)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(2)
    
    subRoot1 = TreeNode(4)
    subRoot1.left = TreeNode(1)
    subRoot1.right = TreeNode(2)
    
    test1 = isSubtree(root1, subRoot1)
    print("Test 1 - Basic subtree match:")
    print("Expected: True")
    print(f"Got: {test1}")
    print(f"Status: {'✓ PASS' if test1 == True else '✗ FAIL'}")
    print()
    
    # Test 2: subRoot is not a subtree (different structure)
    root2 = TreeNode(3)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(2)
    
    subRoot2 = TreeNode(4)
    subRoot2.left = TreeNode(1)
    
    test2 = isSubtree(root2, subRoot2)
    print("Test 2 - Partial structure (not a subtree):")
    print("Expected: False")
    print(f"Got: {test2}")
    print(f"Status: {'✓ PASS' if test2 == False else '✗ FAIL'}")
    print()
    
    # Test 3: Single node - subRoot equals root
    root3 = TreeNode(1)
    subRoot3 = TreeNode(1)
    
    test3 = isSubtree(root3, subRoot3)
    print("Test 3 - Single node match:")
    print("Expected: True")
    print(f"Got: {test3}")
    print(f"Status: {'✓ PASS' if test3 == True else '✗ FAIL'}")
    print()
    
    # Test 4: subRoot is the entire root tree
    root4 = TreeNode(1)
    root4.left = TreeNode(1)
    
    subRoot4 = TreeNode(1)
    subRoot4.left = TreeNode(1)
    
    test4 = isSubtree(root4, subRoot4)
    print("Test 4 - Entire tree matches:")
    print("Expected: True")
    print(f"Got: {test4}")
    print(f"Status: {'✓ PASS' if test4 == True else '✗ FAIL'}")
    print()
    
    # Test 5: Duplicate values but different structure
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.left.left = TreeNode(3)
    
    subRoot5 = TreeNode(2)
    subRoot5.right = TreeNode(3)
    
    test5 = isSubtree(root5, subRoot5)
    print("Test 5 - Duplicate values, different structure:")
    print("Expected: False")
    print(f"Got: {test5}")
    print(f"Status: {'✓ PASS' if test5 == False else '✗ FAIL'}")
    print()


# Run all tests
if __name__ == "__main__":
    run_tests()