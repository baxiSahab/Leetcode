def minWindow(s: str, t: str) -> str:
    n , N , dict_t , temp_dict = len(t) , len(s) , {char: t.count(char) for char in set(t)} , {}
    have, need = 0, len( set(t) ) # how many unique ints needed
    left , right, min_len = 0, 0, N
    answer = []
    while right < N:
        letter = s[right]

        if letter in t:
            temp_dict[letter] = temp_dict.get(letter, 0) + 1 # we update this only if the letter is in dict-t
            if temp_dict[letter] == dict_t[letter]: # if we match the freq we have one more 
                have+=1

        while have == need: # we foind our subs , one of many so we store len and find a new string
                if min_len >=  right-left+1:         
                    min_len = right-left+1
                    answer = [left,right] # we store indeces as we can get len and the sub-string from this

                # now we look for shorter sub string
                temp_dict[s[left]] = temp_dict.get(s[left] , 0) - 1 # remove left end and move it forward
                if s[left] in t and temp_dict[ s[left] ] < dict_t[ s[left] ]: # if we fdrop below the 
                   
                    have-=1 # as we lost one meeting condition remove that
                left+=1
                # we dont move right forward yet
        right+=1 # default case for if letter not in t
    return s[answer[0] : answer[1]+1] if answer else ""
# Test runner
tests = [
    (("ADOBECODEBANC", "ABC"), "BANC"),
    (("a", "a"), "a"),
    (("a", "aa"), ""),
    (("aa", "aa"), "aa"),
    (("AABC", "ABC"), "ABC"),
]

for (s, t), expected in tests:
    result = minWindow(s, t)
    status = "✅" if result == expected else "❌"
    print(f"{status} minWindow({s!r}, {t!r}) = {result!r} (expected {expected!r})")