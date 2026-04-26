from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = dict()
        current = head
        
        while current:
            if current in seen:
                return True
            # elif current.next == None:
            #     return False
            else:
                seen[current] = True
            current = current.next

        return False

# Test Case 1: List WITHOUT a cycle (like your example)
# 1 → 2 → 3 → 4 → None
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)

sol = Solution()
print("Test 1 (no cycle):", sol.hasCycle(head1))  # Should print: False
print("About to run Test 2...")  # Add this

# Test Case 2: List WITH a cycle
head2 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
head2.next = node2
node2.next = node3
node3.next = node2  # Creates cycle back to node 2

print("Test 2 (with cycle):", sol.hasCycle(head2))  # Should print: True
print("Test 2 completed!")  # Add this