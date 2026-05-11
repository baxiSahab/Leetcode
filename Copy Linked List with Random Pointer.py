class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        value_dict = {}

        curr = head
        while curr:
            value_dict[curr] = Node(curr.val)
            curr = curr.next

        copy =  head
        while copy:
            value_dict[copy].next = value_dict[copy.next] if copy.next else None
            value_dict[copy].random = value_dict[copy.random] if copy.random else None
            copy=copy.next

        return value_dict[head]

        


# --- Test Harness ---
def build_list(pairs):
    # pairs: list of [val, random_index] where random_index is None or int
    if not pairs: return None
    nodes = [Node(val) for val, _ in pairs]
    for i, (_, rand_idx) in enumerate(pairs):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
        nodes[i].random = nodes[rand_idx] if rand_idx is not None else None
    return nodes[0]

def verify_deep_copy(original_head, copy_head):
    orig, copy = original_head, copy_head
    orig_nodes = set()
    while orig:
        orig_nodes.add(id(orig))
        orig = orig.next
    while copy:
        assert id(copy) not in orig_nodes, "FAIL: shared node found"
        copy = copy.next
    print("PASS: deep copy verified")

# Test 1: Basic chain, random points forward
h = build_list([[7,None],[13,0],[11,4],[10,2],[1,0]])
verify_deep_copy(h, Solution().copyRandomList(h))

# Test 2: Single node, random points to itself
h = build_list([[1,0]])
verify_deep_copy(h, Solution().copyRandomList(h))

# Test 3: All randoms are None
h = build_list([[3,None],[7,None]])
verify_deep_copy(h, Solution().copyRandomList(h))

# Test 4: Empty list
assert Solution().copyRandomList(None) is None

# Test 5: R++andom points backward
h = build_list([[1,None],[2,0],[3,1]])
verify_deep_copy(h, Solution().copyRandomList(h))