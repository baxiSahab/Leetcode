from collections import deque
from typing import Optional, List

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        answer = []
        level_q = [root]
        level_q = deque([root])
        while level_q:
            L=len(level_q)
            level_vals = []
            for _ in range(0,L):
                item = level_q.popleft()
                level_vals.append(item.val)
                if item.left: level_q.append(item.left)
                if item.right: level_q.append(item.right)
                # print(f'i{i} , levelq{level_q} answer{answer}')

            answer.append(level_vals)
            # print(f'answer{answer} , levelq{level_q}')
        return answer
            
            


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

s = Solution()

t1 = build_tree([3, 9, 20, None, None, 15, 7])
t2 = build_tree([1])
t3 = build_tree([])
t4 = build_tree([])
t5 = build_tree([1, 2, 3, 4, 5, 6, 7])
print(s.levelOrder(t1))  # [[3], [9, 20], [15, 7]]
print(s.levelOrder(t2))  # [[1]]
print(s.levelOrder(t3))  # []
print(s.levelOrder(t4))  # [[1], [2], [3]]
print(s.levelOrder(t5))  # [[1], [2, 3], [4, 5, 6, 7]]