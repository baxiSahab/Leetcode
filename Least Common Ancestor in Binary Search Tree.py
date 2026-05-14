class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pass


# ── Build helpers ──────────────────────────────────────────────
def build_bst(values):
    """Insert list of values into a BST."""
    def insert(root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = insert(root.left, val)
        else:
            root.right = insert(root.right, val)
        return root
    root = None
    for v in values:
        root = insert(root, v)
    return root

def find_node(root, val):
    """Return the TreeNode with given val."""
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


# ── Test cases ─────────────────────────────────────────────────
sol = Solution()

# Test 1: Standard — LCA is the root
#        6
#       / \
#      2   8
#     / \ / \
#    0  4 7  9
root = build_bst([6, 2, 8, 0, 4, 7, 9])
p, q = find_node(root, 2), find_node(root, 8)
result = sol.lowestCommonAncestor(root, p, q)
print(f"Test 1 (expect 6): {result.val}")

# Test 2: LCA is one of the nodes itself (ancestor-descendant)
p, q = find_node(root, 2), find_node(root, 4)
result = sol.lowestCommonAncestor(root, p, q)
print(f"Test 2 (expect 2): {result.val}")

# Test 3: Both nodes on same side
p, q = find_node(root, 7), find_node(root, 9)
result = sol.lowestCommonAncestor(root, p, q)
print(f"Test 3 (expect 8): {result.val}")

# Test 4: Single node tree (p == q == root)
root2 = TreeNode(1)
p, q = root2, root2
result = sol.lowestCommonAncestor(root2, p, q)
print(f"Test 4 (expect 1): {result.val}")

# Test 5: p and q are adjacent (parent-child)
root3 = build_bst([5, 3, 7, 2, 4])
p, q = find_node(root3, 3), find_node(root3, 2)
result = sol.lowestCommonAncestor(root3, p, q)
print(f"Test 5 (expect 3): {result.val}")