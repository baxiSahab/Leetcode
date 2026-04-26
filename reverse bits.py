"""
Reverse Bits - LeetCode 75
Problem: Reverse bits of a given 32-bit unsigned integer.

Example:
Input: n = 00000010100101000001111010011100
Output:    39447139 (00111001011110000010100101000000)

Explanation: The input binary string represents unsigned integer 43261596, 
and if we reverse its bits, we get 964176192 which is 39447139 in decimal.
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Reverse the bits of a 32-bit unsigned integer.
        
        Args:
            n: A 32-bit unsigned integer
            
        Returns:
            The integer with its bits reversed
        """
        # TODO: Add your solution here
        result = 0
        for i in range(32):
            # Extract the bit at position i from the right
            bit = (n >> i) & 1
            
            # Place it at position (31 - i) in the result
            result |= (bit << (31 - i))

        return result


# Test Cases
def run_tests():
    solution = Solution()
    
    # Test Case 1: Basic example from problem
    test1_input = 43261596  # Binary: 00000010100101000001111010011100
    test1_expected = 964176192  # Binary: 00111001011110000010100101000000
    test1_result = solution.reverseBits(test1_input)
    print(f"Test 1: {test1_result == test1_expected}")
    print(f"  Input: {test1_input} (Binary: {bin(test1_input)})")
    print(f"  Expected: {test1_expected} (Binary: {bin(test1_expected)})")
    print(f"  Got: {test1_result} (Binary: {bin(test1_result)})")
    print()
    
    # Test Case 2: All zeros (edge case)
    test2_input = 0
    test2_expected = 0
    test2_result = solution.reverseBits(test2_input)
    print(f"Test 2: {test2_result == test2_expected}")
    print(f"  Input: {test2_input} (Binary: {bin(test2_input)})")
    print(f"  Expected: {test2_expected} (Binary: {bin(test2_expected)})")
    print(f"  Got: {test2_result} (Binary: {bin(test2_result)})")
    print()
    
    # Test Case 3: All ones (edge case)
    test3_input = 0xFFFFFFFF  # 4294967295 - all 32 bits are 1
    test3_expected = 0xFFFFFFFF  # Reversing all 1s gives all 1s
    test3_result = solution.reverseBits(test3_input)
    print(f"Test 3: {test3_result == test3_expected}")
    print(f"  Input: {test3_input} (Binary: {bin(test3_input)})")
    print(f"  Expected: {test3_expected} (Binary: {bin(test3_expected)})")
    print(f"  Got: {test3_result} (Binary: {bin(test3_result)})")
    print()
    
    # Test Case 4: Single bit at start
    test4_input = 0x80000000  # 2147483648 - only leftmost bit is 1
    test4_expected = 0x00000001  # 1 - only rightmost bit is 1
    test4_result = solution.reverseBits(test4_input)
    print(f"Test 4: {test4_result == test4_expected}")
    print(f"  Input: {test4_input} (Binary: {bin(test4_input)})")
    print(f"  Expected: {test4_expected} (Binary: {bin(test4_expected)})")
    print(f"  Got: {test4_result} (Binary: {bin(test4_result)})")
    print()
    
    # Test Case 5: Single bit at end
    test5_input = 0x00000001  # 1 - only rightmost bit is 1
    test5_expected = 0x80000000  # 2147483648 - only leftmost bit is 1
    test5_result = solution.reverseBits(test5_input)
    print(f"Test 5: {test5_result == test5_expected}")
    print(f"  Input: {test5_input} (Binary: {bin(test5_input)})")
    print(f"  Expected: {test5_expected} (Binary: {bin(test5_expected)})")
    print(f"  Got: {test5_result} (Binary: {bin(test5_result)})")
    print()


if __name__ == "__main__":
    run_tests()