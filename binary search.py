def search(nums: list[int], target: int , left = 0 , right = None) -> int:
    if right == None:
        right=len(nums)-1

    if left > right: # we have excited the loop basically
        return -1
    m = (left + right) // 2
    if nums[m] == target:
        return m

    
    if target < nums[m]:
        return search(nums , target , left, right = m-1)
    elif target > nums[m]:
        return search(nums , target , left = m+1 , right=right)

    # if right == None:
    #     right = len(nums) - 1
    # n = (right - left) // 2 + left
    # if target == nums[right]: return right
    # if target == nums[left]: return left
    # if target == nums[n]: return n
    # elif left == right: return -1
   

    # if target < nums[(right - left) // 2 + left]:
    #     return search(nums , target , left = left , right =(right - left) // 2 + left)
    # else:
    #     return search( nums  , target , left = (right - left) // 2 + left +1, right=right)


    # return i for i in range len(nums) if nums[i] == target else -1

print(search([1, 3, 5, 7, 9], 5) )   # → 2
print(search([1, 3, 5, 7, 9], 1) )     # → 0  (left boundary)
print(search([1, 3, 5, 7, 9], 9) )     # → 4  (right boundary)
print(search([1, 3, 5, 7, 9], 4) )     # → -1 (not in array)
print(search([5], 5)    )               # → 0  (single element)