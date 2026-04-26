def longestConsecutive(nums):
    """
    Find the length of the longest consecutive elements sequence.
    
    Args:
        nums: List of integers (can contain duplicates and be unsorted)
    
    Returns:
        Integer representing the length of the longest consecutive sequence
    """
    # YOUR CODE HERE
    count = 0
    max_count = [0]
    nums=sorted(nums)

    if not nums: # base case empty
        return 0
    
    for i in range(len(nums) - 1):

        if nums[i] == nums[i+1]: # deosnt break streak if 0,0,1 or 9,10,10,11
            continue

        elif  nums[i+1] != nums[i] + 1:  # if mul. seq, saves all of them
            max_count.append(count)
            count = 0

            # print(max_count,count)
        else:
            count+=1

    max_count.append(count) # saves last count if it lasts till end of array
    return max(max_count)+1 # accounting for missing the count for first 2 of a seq.

# Test cases
def test_longestConsecutive():
    test_cases = [
        # (input, expected_output, description)
        ([100, 4, 200, 1, 3, 2], 4, "Basic case: [1,2,3,4] is the longest sequence"),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9, "Sequence from 0-8"),
        ([], 0, "Empty list"),
        ([1], 1, "Single element"),
        ([1, 1, 1, 1], 1, "All duplicates"),
        ([9, 1,4,7, 3,2,8,5,6], 9, "1-9 out of order"),
        ([1, 2, 0, 1], 3, "Duplicates with sequence [0,1,2]"),
        ([-1, 0, 1, 2, 3], 5, "Sequence with negative numbers"),
        ([50, 51], 2, "Two consecutive numbers"),
        ([1, 100, 101, 102, 103], 4, "Two separate sequences"),
    ]
    
    passed = 0
    failed = 0
    
    for i, (nums, expected, description) in enumerate(test_cases, 1):
        result = longestConsecutive(nums)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        
        if result == expected:
            passed += 1
        else:
            failed += 1
        
        print(f"Test {i}: {status}")
        print(f"  Description: {description}")
        print(f"  Input: {nums}")
        print(f"  Expected: {expected}, Got: {result}")
        print()
    
    print(f"\n{'='*50}")
    print(f"Results: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    test_longestConsecutive()