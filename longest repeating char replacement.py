def characterReplacement(s: str, k: int) -> int:
    left , right , N , freq , max_s = 0, 1 , len(s), {}, 0
    freq[s[left]] = freq.get(s[left],0) + 1
    if N == 1 and s[left].isalpha() == True:
        return 1
    while right < N:
        window_len = right - left + 1
        freq[s[right]] = freq.get(s[right], 0) + 1
        if window_len - max(freq.values()) <= k:
            max_s = max(max_s , window_len)
            right+=1
        else:
            # print('we are hitting else')
            freq[s[left]] = freq.get(s[left]) - 1 # removing the head of window and sliding it
            left+=1
            right+=1
        
        # print(left, right, max_s, freq)
            
    return max_s
# # Test cases
print(characterReplacement("ABAB", 2))   # 4
print(characterReplacement("AABABBA", 1)) # 4
print(characterReplacement("AAAA", 2))   # 4
print(characterReplacement("ABCD", 1))   # 2
print(characterReplacement("A", 0))      # 1