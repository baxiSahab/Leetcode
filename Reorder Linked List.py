from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    if not head or not head.next:
        return head
    slow , fast = head , head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = None
    middle = slow

    reverse = reverseList(middle)
    first=head

    while first and reverse:
        tmp1 = first.next
        tmp2 = reverse.next

        first.next = reverse
        reverse.next = tmp1

        prev = reverse
        first = tmp1
        reverse = tmp2

    if reverse == None:
        prev.next = first
    if first == None and reverse != None:
        prev.next = reverse
def reverseList(head):
    curr = head
    prev = None

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


# ---- Test Harness ----
def build(vals):
    if not vals: return None
    head = ListNode(vals[0])
    cur = head
    for v in vals[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head

def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

tests = [
    [1, 2, 3, 4],        # Expected: [1, 4, 2, 3]
    [1, 2, 3, 4, 5],     # Expected: [1, 5, 2, 4, 3]
    [1],                 # Expected: [1]
    [1, 2],              # Expected: [1, 2]
    [1, 2, 3],           # Expected: [1, 3, 2]
]

for t in tests:
    head = build(t)
    reorderList(head)
    print(to_list(head))