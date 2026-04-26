def trap(height: list[int]) -> int:
    N = len(height)
    i, j , water = 0 , N-1 , 0
    max_left, max_right = 0, 0

    while i<j:
        if max_left <= max_right:
            water+= max(0, max_left - height[i])
            max_left = max(max_left, height[i])
    
            i+=1
        else:
            water += max(0, max_right - height[j])
            max_right = max(max_right, height[j])
            
            j-=1
        
        # if excist loop calc water above j
    water += max(0, min(max_right , max_left) - height[j])
    return water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Expected: 6
print(trap([4,2,0,3,2,5]))               # Expected: 9
print(trap([1,0,1]))                     # Expected: 1
print(trap([3,0,0,2,0,4]))              # Expected: 10
print(trap([1]))                         # Expected: 0