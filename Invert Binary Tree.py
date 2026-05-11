from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        lefty = root.left
        righty = root.right

        # if root.left:
        root.right = lefty
        # if root.right:
        root.left = righty
        self.invertTree(righty)
        self.invertTree(lefty)
        
        # print(to_list(root))
        return root
    
def build_tree(vals):
    if not vals:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in vals]
    for i, n in enumerate(nodes):
        if n:
            if 2*i+1 < len(nodes): n.left = nodes[2*i+1]
            if 2*i+2 < len(nodes): n.right = nodes[2*i+2]
    return nodes[0]

def to_list(root):
    if not root: return []
    res, q = [], [root]
    while q:
        n = q.pop(0)
        res.append(n.val if n else None)
        if n:
            q.append(n.left)
            q.append(n.right)
    return res

s = Solution()
print(to_list(s.invertTree(build_tree([4,2,7,1,3,6,9]))) == [4,7,2,9,6,3,1])  # True
print(to_list(s.invertTree(build_tree([2,1,3])))          == [2,3,1])           # True
print(to_list(s.invertTree(build_tree([])))               == [])                # True
print(to_list(s.invertTree(build_tree([1])))              == [1])               # True
print(to_list(s.invertTree(build_tree([1,2])))            == [1,None,2])        # True