def twoSum(numbers: list[int], target: int) -> list[int]:
    i , j = 0 , len(numbers)-1
    while i<j:
        if numbers[i] + numbers[j] > target:
            j-=1
        elif numbers[i] + numbers[j] < target:
            i+=1
        else: return i,j,numbers[i],numbers[j]

# 1. Basic case
print(twoSum([2, 7, 11, 15], 9))     # → [1, 2]

# 2. Adjacent elements
print(twoSum([1, 2, 3, 4], 3)  )        # → [1, 2]

# 3. First and last
print(twoSum([1, 3, 5, 8], 9)   )       # → [2, 4]

# 4. Negative numbers
print(twoSum([-3, -1, 0, 2, 5], 1)  )   # → [2, 5]

# 5. Two elements only
print(twoSum([1, 5], 6)   )              # → [1, 2]


# nums = [1, 2, 3, 4, 5]
# target = 5u
# for i in range(len(nms)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print([i,j])
#             break
#         else:
# 1. Basic case
