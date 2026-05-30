def twoSum(nums, target):
    """
    Find two numbers that add up to target.
    Return the indices of the two numbers.
    
    Complexity:
        Time: O(n) - single pass through array
        Space: O(n) - hash map storage
    
    Args:
        nums: List of integers
        target: Target sum
    
    Returns:
        List of two indices [i, j] where nums[i] + nums[j] == target
    """
    # YOUR CODE HERE

    hashmap ={}

    for key , value in enumerate(nums):
        hashmap[value] = key

    for i , n in enumerate(nums):
        remainder = target - n
        if remainder in hashmap and hashmap[remainder] != i:
            return [ i , hashmap[remainder] ]
    

test_cases = [
    # (nums, target, expected_output)
    ([2, 7, 11, 15], 9, [0, 1]),           # Basic case
    ([3, 2, 4], 6, [1, 2]),                # Different order
    ([3, 3], 6, [0, 1]),                   # Duplicate values
    ([1, 2, 3, 4, 5], 9, [3, 4]),          # Larger list
    ([-1, -2, -3, 5, 10], 7, [3, 4]),      # Negative numbers
    ([1000000, 2], 1000002, [0, 1]),       # Large numbers
]


def run_tests():
    print("Running Two Sum Tests\n" + "="*50)
    passed = 0
    failed = 0
    
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = twoSum(nums, target)
        
        # Check if result is valid (handles both [i,j] and [j,i])
        is_correct = (result is not None and 
                     sorted(result) == sorted(expected) and
                     nums[result[0]] + nums[result[1]] == target)
        
        status = "✓ PASS" if is_correct else "✗ FAIL"
        print(f"Test {i}: {status}")
        print(f"  Input: nums={nums}, target={target}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
        
        if is_correct:
            passed += 1
        else:
            failed += 1
        print()
    
    print("="*50)
    print(f"Results: {passed} passed, {failed} failed")
    return passed, failed


if __name__ == "__main__":
    run_tests()


# soltion 1
# for i in range(len(nums)):
#         remainder = target - nums[i]

#         if remainder in nums[i+1:]:
#             return [i,nums.index(remainder, i+1)]