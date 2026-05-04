def search(nums, target):
    l , r = 0 , len(nums) - 1
    m = 0
    while l<r:
        m = (l+r)//2

        if nums[m] == target: return m

        if nums[m] < nums[r]:
            if nums[m] <= target <= nums[r]: #right is sorted right way and target is there
                l = m+1
                # print('here',nums[l])
            else: r=m # sorted but its not there
        
        if nums[m] >= nums[r]: # right unsorted 
            if target < nums[r]: # unsort right but target in between
                l = m + 1
            else: 
                r=m # prob in left 

    return l if target == nums[l] else -1

# Test cases
print(search([4,5,6,7,0,1,2], 0))   # Expected: 4
print(search([4,5,6,7,0,1,2], 3))   # Expected: -1
print(search([1], 0))               # Expected: -1
print(search([1], 1))               # Expected: 0
print(search([3,1,2], 1))           # Expected: 1
print(search([1,3] , 3))