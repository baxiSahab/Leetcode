from typing import List
from math import floor

def isPalindrome(s: str) -> bool:

    s = ''.join(char for char in s if char.isalpha()).lower()
    # front , back 
    n=len(s)
    for i in range(floor(n/2)):
        if s[i] == s[n - i - 1]:
            # print(f'i , {s[i]} , other {s[n-i-1]}')
            # front+=1
            # back-=1
            i+=1
        else: return False
    return True

    # s = ''.join([char for char in s if char.isalnum()])
    # s=s.lower()
    # n=len(s)
    
    # for i in range(n//2):
    #     if s[i] == s[n-1 - i]:
    #         continue
    #     else:
    #         return False
    # return True

# Test cases
print(isPalindrome("A man, a plan, a canal: Panama"))  # True
print(isPalindrome("race a car"))                       # False
print(isPalindrome(" "))                                # True
print(isPalindrome("Was it a car or a cat I saw?"))    # True
print(isPalindrome("0P"))                               # False