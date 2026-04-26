from typing import List

def isPalindrome(s: str) -> bool:
    s = ''.join([char for char in s if char.isalnum()])
    s=s.lower()
    n=len(s)
    
    for i in range(n//2):
        if s[i] == s[n-1 - i]:
            continue
        else:
            return False
    return True

# Test cases
print(isPalindrome("A man, a plan, a canal: Panama"))  # True
print(isPalindrome("race a car"))                       # False
print(isPalindrome(" "))                                # True
print(isPalindrome("Was it a car or a cat I saw?"))    # True
print(isPalindrome("0P"))                               # False