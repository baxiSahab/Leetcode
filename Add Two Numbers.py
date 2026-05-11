from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        remainder = 0
        output = ListNode(0)
        copy = output
        while l1 or l2 or remainder:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum = v1 + v2 + remainder
            remainder = 0

            if sum >=10:
                remainder = sum // 10
                sum = sum % 10
        
            output.next = ListNode(sum)
            output = output.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return copy.next


# --- Test Harness ---
def make_list(nums):
    dummy = ListNode(0)
    cur = dummy
    for n in nums:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next

def list_to_arr(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test 1: 342 + 465 = 807  → [7,0,8]
l1, l2 = make_list([2,4,3]), make_list([5,6,4])

# Test 2: 0 + 0 = 0  → [0]
l1, l2 = make_list([0]), make_list([0])

# Test 3: 9999999 + 9999 = 10009998  → [8,9,9,9,0,0,0,1]
l1, l2 = make_list([9,9,9,9,9,9,9]), make_list([9,9,9,9])

# Test 4: Different lengths — 5 + 64 = 69  → [9,6]
l1, l2 = make_list([5]), make_list([4,6])

# Test 5: Carry at final position — 5 + 5 = 10  → [0,1]
l1, l2 = make_list([5]), make_list([5])

sol = Solution()

print(list_to_arr(sol.addTwoNumbers(make_list([2,4,3]), make_list([5,6,4]))))       # [7,0,8]
print(list_to_arr(sol.addTwoNumbers(make_list([0]), make_list([0]))))                # [0]
print(list_to_arr(sol.addTwoNumbers(make_list([9,9,9,9,9,9,9]), make_list([9,9,9,9]))))  # [8,9,9,9,0,0,0,1]
print(list_to_arr(sol.addTwoNumbers(make_list([5]), make_list([4,6]))))              # [9,6]
print(list_to_arr(sol.addTwoNumbers(make_list([5]), make_list([5]))))                # [0,1]