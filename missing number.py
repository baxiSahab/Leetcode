from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Find the missing number in array containing n distinct numbers in range [0, n].
        
        Args:
            nums: List of integers
            
        Returns:
            The missing number
        """
        # TODO: Write your solution here
        d = {i: False for i in range(len(nums)+1)}

        for number in nums:
            d[number] = True

        return [key for key, value in d.items() if value == False][0]
            


def test_missing_number():
    """Test cases for the missingNumber solution"""
    solution = Solution()
    
    test_cases = [
        # (input, expected_output, description)
        ([3, 0, 1], 2, "Missing number in middle"),
        ([0, 1, 3], 2, "Missing number at end"),
        ([0, 1], 2, "Small array missing 2"),
        ([1], 0, "Single element, missing 0"),
        ([0], 1, "Single element, missing 1"),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8, "Larger unsorted array"),
        ([0, 1, 2, 3, 4], 5, "Missing largest number (n)"),
        ([3, 0, 1, 2, 5, 6, 7, 8, 9], 4, "Missing from middle of larger array"),
    ]
    
    passed = 0
    failed = 0
    
    for nums, expected, description in test_cases:
        result = solution.missingNumber(nums)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        
        print(f"{status} | {description}")
        print(f"       Input: {nums}")
        print(f"       Expected: {expected}, Got: {result}")
        print()
        
        if result == expected:
            passed += 1
        else:
            failed += 1
    
    print(f"\n{'='*50}")
    print(f"Results: {passed} passed, {failed} failed out of {passed + failed} total")
    print(f"{'='*50}")
    
    return failed == 0


if __name__ == "__main__":
    test_missing_number()