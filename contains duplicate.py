def containsDuplicate(nums):
    """
    Given an integer array nums, return True if any value appears 
    at least twice in the array, and return False if every element is distinct.
    """
    # YOUR CODE HERE
    for i in range(len(nums)):

        removed = nums[i]
        nums[i] = 'None'
        # print(i, removed)

        if removed in nums:
            return True
        
    return False



# Test cases
def run_tests():
    test_cases = [
        # (input, expected_output)
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([99, 99], True),
        ([1], False),
        ([], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([0, 4, 4, 0, 0, 6, 5, 0, 0, 7, 0, 5, 4, 4, 0], True),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], False),
        ([-1,2,-3,2], True),
    ]
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = containsDuplicate(nums)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"Test {i}: {status}")
        print(f"  Input: {nums}")
        print(f"  Expected: {expected}, Got: {result}\n")


if __name__ == "__main__":
    run_tests()