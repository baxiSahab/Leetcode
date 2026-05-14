from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right





class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        node = root
        subnode = subRoot

        if not node and not subnode: return True
        if node and not subnode: return True
        if not node and subnode: return False
     
        # if self.isSameTree(node , subnode):
        #     return self.isSameTree(node , subnode)
        # else: return self.isSubtree(node.left , subnode) or self.isSubtree( node.right , subnode)
        
        return self.isSameTree(node, subnode) or self.isSubtree(node.left, subnode) or self.isSubtree(node.right, subnode)


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q: return True

        if p and not q: return False
        if not p and q: return False

        pp = p.val
        qq = q.val

        if pp == qq:
            return self.isSameTree(p.right , q.right) and self.isSameTree(p.left , q.left)

        else: return False


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(vals):
    if not vals:
        return None
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    while q and i < len(vals):
        node = q.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            q.append(node.right)
        i += 1
    return root

sol = Solution()
print(sol.isSubtree(build_tree([3,4,5,1,2]), build_tree([4,1,2])))   # True
print(sol.isSubtree(build_tree([3,4,5,1,2,None,None,None,None,0]), build_tree([4,1,2])))  # False
print(sol.isSubtree(build_tree([1,2,3]), build_tree([1,2,3])))        # True
print(sol.isSubtree(build_tree([1,2,3]), build_tree([])))             # True
print(sol.isSubtree(build_tree([1,2,3,4]), build_tree([4])))          # True