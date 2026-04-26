# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    """
    Merge two sorted linked lists into one sorted linked list.
    
    Args:
        list1: Head of first sorted linked list (or None)
        list2: Head of second sorted linked list (or None)
    
    Returns:
        Head of the merged sorted linked list
    
    TODO: Write your solution here
    """
    dummy = ListNode(0)
    merged_list = dummy

    while list1 is not None and list2 is not None:
        # print(list1.val,list2.val)
        if list1.val < list2.val:
            merged_list.next = list1
            list1 = list1.next
        else:
            merged_list.next = list2
            list2 = list2.next
        merged_list = merged_list.next
        
    if list1 is not None:
        merged_list.next = list1

    if list2 is not None:
        merged_list.next = list2

    return dummy.next
                


# ============== HELPER FUNCTIONS (Don't modify) ==============

def create_linked_list(arr):
    """Convert array to linked list"""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_array(head):
    """Convert linked list to array for easy comparison"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_solution():
    """Run all test cases"""
    test_cases = [
        # (list1, list2, expected)
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([],        [],        []),
        ([],        [0],       [0]),
        ([1],       [0],       [0, 1]),
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([2, 5, 8], [1, 3, 4], [1, 2, 3, 4, 5, 8]),
        ([5],       [1, 2, 3, 4], [1, 2, 3, 4, 5]),
    ]
    
    passed = 0
    failed = 0
    
    for i, (list1_arr, list2_arr, expected) in enumerate(test_cases, 1):
        list1 = create_linked_list(list1_arr)
        list2 = create_linked_list(list2_arr)
        
        result = mergeTwoLists(list1, list2)
        result_arr = linked_list_to_array(result)
        
        if result_arr == expected:
            print(f"✓ Test {i} PASSED")
            passed += 1
        else:
            print(f"✗ Test {i} FAILED")
            print(f"  Input:    list1={list1_arr}, list2={list2_arr}")
            print(f"  Expected: {expected}")
            print(f"  Got:      {result_arr}")
            failed += 1
    
    print(f"\n{passed}/{len(test_cases)} tests passed")
    return failed == 0

if __name__ == "__main__":
    test_solution()