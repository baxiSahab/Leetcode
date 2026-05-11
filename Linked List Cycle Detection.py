from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        visited = []
        while curr:
            if curr in visited:
                return True
            visited.append(curr)
            curr = curr.next

        return False

# ---------- Test Harness ----------
def build_list(values, pos):
    """Build linked list; pos = index where tail connects (-1 = no cycle)."""
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]

sol = Solution()

# Test 1: Basic cycle (tail -> index 1)
assert sol.hasCycle(build_list([3, 2, 0, -4], 1)) == True

# Test 2: Two-node cycle (tail -> head)
assert sol.hasCycle(build_list([1, 2], 0)) == True

# Test 3: No cycle
assert sol.hasCycle(build_list([1, 2, 3], -1)) == False

# Test 4: Single node, no cycle
assert sol.hasCycle(build_list([1], -1)) == False

# Test 5: Empty list
assert sol.hasCycle(None) == False

print("All tests passed!")