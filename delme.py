class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


dummy = ListNode(0)
dummy = dummy.next
print(dummy.val)

# counted = Counter(nums)
# return [ x[0] for x in sorted(counted.items() , key = lambda x:x[1], reverse=True)[:k] ]