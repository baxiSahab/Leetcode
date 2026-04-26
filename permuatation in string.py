def checkInclusion(s1: str, s2: str) -> bool:

    left , n , N ,  s1_dict= 0 , len(s1), len(s2) , {char: s1.count(char) for char in set(s1)}
    right = left + n

    if n > N:
        return False
    if s1 == s2:
        return True
    while right <= N:
        temp_dict = { char: s2[left:right].count(char) for char in set(s2[left:right]) }
        # print(s1_dict , temp_dict, left, right)

        if temp_dict == s1_dict:
            # print(temp_dict,'1')
            return True
        else:
            # print(temp_dict,'2')
            left+=1
            # if left+n < N:
            right = left + n

    return False


# Test cases
print(checkInclusion("ab", "eidbaooo"))   # True  ("bao" contains "ab" permuted as "ba")
print(checkInclusion("ab", "eidboaoo"))   # False
print(checkInclusion("a", "a"))           # True
print(checkInclusion("abc", "bbbca"))     # True  ("bca" is a permutation of "abc")
print(checkInclusion("hello", "hi"))      # False (s1 longer than s2)