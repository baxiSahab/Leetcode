class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    cur = head
    head.next = None
    while cur:
        
        cur = cur.next

# --- Test Harness ---
def build_list(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    cur = head
    for v in vals[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head

def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test cases
print(print_list(reverseList(build_list([1,2,3,4,5]))))  # [5,4,3,2,1]
print(print_list(reverseList(build_list([1,2]))))         # [2,1]
print(print_list(reverseList(build_list([1]))))           # [1]
print(print_list(reverseList(build_list([]))))            # []
print(print_list(reverseList(build_list([1,1,1]))))       # [1,1,1]