from collections import Counter
def isAnagram(s: str, t: str) -> bool:
    n1 , n2 = len(s) , len(t)

    if n1 != n2: return False

    dict1 , dic2 = Counter(s) , Counter(t)
    if dict1 != dic2: return False
    return True

print(isAnagram("anagram", "nagaram"))  # True
print(isAnagram("rat", "car"))          # False
print(isAnagram("a", "a"))             # True  (single char, same)
print(isAnagram("a", "b"))             # False (single char, diff)
print(isAnagram("ab", "a"))            # False (different lengths)

