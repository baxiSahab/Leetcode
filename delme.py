class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


dummy = ListNode(0)
dummy = dummy.next
print(dummy.val)

