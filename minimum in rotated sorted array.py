def findMin(nums: list[int]) -> int:
    l,r = 0 , len(nums) - 1
    
    while l<r:
        mid = (l+r)//2
        # print(f'{nums[mid]} this is mid {nums[r]}')
        if nums[mid] > nums[r]: #implies roation created a bid drop in between mid and r; so min is on right 
            l = mid+1
        else: # min must be on the left
            r = mid
    return nums[l] # or nums r



# Test cases
print(findMin(nums=[3,4,5,6,1,2]))   # Expected: 1
print(findMin(nums=[4,5,0,1,2,3]))  # Expected: 0
print(findMin([1]))                 # Expected: 1
print(findMin([2, 1]))              # Expected: 1
print(findMin([2, 3, 4, 5]))    # Expected: 1  (no rotation)