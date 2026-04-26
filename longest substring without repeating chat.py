def lengthOfLongestSubstring(s: str) -> int:
    left,right, N , max_s, checker = 0,1, len(s), 0 , []
    if s == '':
        return 0
    
    for right in range(N):
        while s[right] in checker:
            checker.remove(s[left])
            left+=1
        checker.append(s[right])
        # print(checker, right, left)
        
        max_s = max(max_s, right - left+1)
    return max_s
       


print(lengthOfLongestSubstring("abcabcbb"))  # 3  → "abc"
print(lengthOfLongestSubstring("bbbbb"))     # 1  → "b"
print(lengthOfLongestSubstring("pwwkew"))    # 3  → "wke"
print(lengthOfLongestSubstring(""))          # 0
print(lengthOfLongestSubstring("abcde"))     # 5  → whole string