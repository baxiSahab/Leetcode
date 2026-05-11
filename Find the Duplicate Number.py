def findDuplicate(nums: list[int]) -> int:
    slow , fast = 0 , 0

    while True:
        slow = nums[slow]
        fast = nums[ nums[fast] ]
        # print(f'slow= {slow} fast = {fast}')
        if slow == fast:
            break

    slow = 0 #reset
    i=0
    while True:
        slow = nums[slow]
        fast = nums[fast]
        # i+=1
        if slow == fast:
            # print(f'{i} helo')
            break

    return fast



# Test cases
print(findDuplicate([1, 3, 4, 2, 2]))  # 2
print(findDuplicate([3, 1, 3, 4, 2]))  # 3
print(findDuplicate([3, 3, 3, 3, 3]))  # 3
print(findDuplicate([1, 1]))           # 1
print(findDuplicate([2, 2, 2, 1, 3])) # 2