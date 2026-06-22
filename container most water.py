def maxArea(heights: list[int]) -> int:
    max_water = 0
    right = len(heights)-1
    left = 0
    while right > left:
        water = (right - left) * min(heights[right] , heights[left])
        max_water = max(max_water , water)
        if heights[right] < heights[left]: right-=1
        else: left+=1
    return max_water
    # max_area = 0
    # N = len(heights)
    # i=0
    # j=N-1
    # while i < j:

    #     area = (j-i) * min( heights[j] , heights[i] )
    #     if max_area<area:
    #         max_area=area

    #     if heights[j] > heights[i]:
    #         i+=1
    #         # j+=i
    #     else:
    #         j-=1
    # return max_area
test_cases = [
    ([1,8,6,2,5,4,8,3,7], 49),
    ([1,1], 1),
    ([4,3,2,1,4], 16),
    ([1,2,1], 2),
    ([1,8,100,2,100,4,8,3,7], 200),
]

for height, expected in test_cases:
    result = maxArea(height)
    assert result == expected, f"Input: {height}, Expected: {expected}, Got: {result}"
    print(f"✓ PASS: {height} -> {result}")