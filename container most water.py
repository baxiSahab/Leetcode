def maxArea(heights: list[int]) -> int:
    max_area = 0
    N = len(heights)
    i=0
    j=N-1
    while i < j:

        area = (j-i) * min( heights[j] , heights[i] )
        if max_area<area:
            max_area=area

        if heights[j] > heights[i]:
            i+=1
            # j+=i
        else:
            j-=1
    return max_area
# Test 1: Basic case
assert maxArea([1,8,6,2,5,4,8,3,7]) == 49
# Test 2: Two elements
assert maxArea([1,1]) == 1
# Test 3: Decreasing heights
assert maxArea([4,3,2,1]) == 4
# Test 4: Large gap with small heights
assert maxArea([2,3,4,5,18,17,6]) == 17
# Test 5: All same height
assert maxArea([5,5,5,5]) == 15

print("All tests passed!")