def groupAnagrams(strs):
    joined_dict = {}
    
    for word in strs:
        key = ''.join( sorted(word) )
        if key not in joined_dict: joined_dict[key] = []
        if key == ''.join( sorted(word) ): joined_dict[key].append(word)
    return joined_dict.values()
# Quick test
result = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print("Result:", result)
print("Type:", type(result))
print("Length:", len(result))


# for word in strs:
#     key = ''.join(sorted(word))
#     if key not in joined_dict:
#         joined_dict[key] = []
#     joined_dict[key].append(word)

# return list(joined_dict.values())
