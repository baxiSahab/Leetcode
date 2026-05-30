def encode(strs):
    """
    Encodes a list of strings into a single string.
    
    Args:
        strs: List of strings to encode
    
    Returns:
        Single encoded string
    """
    # Your code here
    encoded = []
    for word in strs:
        n = len(word)
        encoded.append(f'{n}#{word}')
    return encoded


def decode(s):
    """
    Decodes a single string back into a list of strings.
    
    Args:
        s: Encoded string
    
    Returns:
        List of decoded strings
    """
    # Your code here
    decoded = []
    i=0
    while i < len(s):
        if s[i] == '#' and s[i-1].isdigit():
            j=i
            n = s[i-1]
            while s[j] != '#':
                j+=1
                word = s[j: j+n + 1]
                decode.append(word)
                i = j + n + 1
    return decoded   
# Test cases
if __name__ == "__main__":
    # Test 1: Basic case
    test1 = ["hello", "world"]
    encoded1 = encode(test1)
    decoded1 = decode(encoded1)
    print(f"Test 1: {test1}")
    print(f"Encoded: {encoded1}")
    print(f"Decoded: {decoded1}")
    print(f"Pass: {test1 == decoded1}\n")
    
    # Test 2: Strings with special characters
    test2 = ["hello,world", "test#123"]
    encoded2 = encode(test2)
    decoded2 = decode(encoded2)
    print(f"Test 2: {test2}")
    print(f"Encoded: {encoded2}")
    print(f"Decoded: {decoded2}")
    print(f"Pass: {test2 == decoded2}\n")
    
    # Test 3: Empty strings
    test3 = ["", "a", ""]
    encoded3 = encode(test3)
    decoded3 = decode(encoded3)
    print(f"Test 3: {test3}")
    print(f"Encoded: {encoded3}")
    print(f"Decoded: {decoded3}")
    print(f"Pass: {test3 == decoded3}\n")
    
    # Test 4: Single string
    test4 = ["hello"]
    encoded4 = encode(test4)
    decoded4 = decode(encoded4)
    print(f"Test 4: {test4}")
    print(f"Encoded: {encoded4}")
    print(f"Decoded: {decoded4}")
    print(f"Pass: {test4 == decoded4}\n")
    
    # Test 5: All empty strings
    test5 = ["", "", ""]
    encoded5 = encode(test5)
    decoded5 = decode(encoded5)
    print(f"Test 5: {test5}")
    print(f"Encoded: {encoded5}")
    print(f"Decoded: {decoded5}")
    print(f"Pass: {test5 == decoded5}\n")
    
    # Test 6: Strings with spaces and symbols
    test6 = ["a b c", "def#ghi", ""]
    encoded6 = encode(test6)
    decoded6 = decode(encoded6)
    print(f"Test 6: {test6}")
    print(f"Encoded: {encoded6}")
    print(f"Decoded: {decoded6}")
    print(f"Pass: {test6 == decoded6}\n")


#         encoded = ''
#     for item in strs:
#         n = len(item)
#         encoded += f'{n}@{item}'

#     return encoded
#  decoded = []
#     i=0
#     while i < len(s):
#         j=i
#         while s[j] != '@':
#             j += 1
#         L = int(s[i:j])
#         word = s[j+1:j+L+1]
#         decoded.append(word)
#         i = L + j +1
#     return decoded

