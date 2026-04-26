class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Your logic here
        charS_count = {}
        charT_count = {}

        for charS in s:
            if charS in charS_count:
                charS_count[charS] +=1
            else:
                charS_count[charS] = 1

        for charT in t:
            if charT in charT_count:
                charT_count[charT] +=1
            else:
                charT_count[charT] = 1

        return charS_count == charT_count
# Test cases
def test_isAnagram():
    solution = Solution()
    
    # Test case 1: Basic anagram
    assert solution.isAnagram("anagram", "nagaram") == True, "Test 1 failed"
    print("✓ Test 1 passed: 'anagram' and 'nagaram'")
    
    # Test case 2: Not an anagram
    assert solution.isAnagram("rat", "car") == False, "Test 2 failed"
    print("✓ Test 2 passed: 'rat' and 'car'")
    
    # Test case 3: Empty strings
    assert solution.isAnagram("", "") == True, "Test 3 failed"
    print("✓ Test 3 passed: empty strings")
    
    # Test case 4: Different lengths
    assert solution.isAnagram("ab", "a") == False, "Test 4 failed"
    print("✓ Test 4 passed: different lengths")
    
    # Test case 5: Single character match
    assert solution.isAnagram("a", "a") == True, "Test 5 passed"
    print("✓ Test 5 passed: single character match")
    
    # Test case 6: Repeated characters
    assert solution.isAnagram("aa", "bb") == False, "Test 6 failed"
    print("✓ Test 6 passed: repeated characters (no match)")
    
    # Test case 7: Repeated characters that are anagrams
    assert solution.isAnagram("aab", "baa") == True, "Test 7 failed"
    print("✓ Test 7 passed: repeated characters (anagram)")
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_isAnagram()