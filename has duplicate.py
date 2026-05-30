def hasDuplicate(nums: list[int]) -> bool:
    copy =[]
    for _ in range(len(nums)):
        if nums[_] in copy:
            # print(nums , )
            return True
        copy.append(nums[_])

    return False


print(hasDuplicate([1, 2, 3, 3]))      # True
print(hasDuplicate([1, 2, 3, 4]))      # False
print(hasDuplicate([1]))               # False  (single element)
print(hasDuplicate([]))                # False  (empty array)
print(hasDuplicate([1, 1, 1, 1]))      # True   (all same)