def threeSum(nums):
    # YOUR SOLUTION HERE
    nums.sort()
    N = len(nums)
    output =[]
    for i in range(N):
        target = -nums[i]
        left = i+1
        right = N-1
        if i>0 and nums[i] == nums[i-1]: continue
        while left < right:
        
            if nums[left] + nums[right] == target:
                output.append([nums[left],nums[right],nums[i]])
                left+=1
                right-=1
                while left+1<=right and nums[left] == nums[left-1]: left+=1
                while right>=left+1 and nums[right] == nums[right+1]: right-=1
            elif nums[left] + nums[right] > target: right-=1
            elif nums[left] + nums[right] < target: left+=1
            
    return output
 

    
    # nums.sort()
    # N = len(nums)
    # answer = []
    # for i in range(N):
    #     left = i+1
    #     right = N - 1
    #     target = nums[i]
    #     if i > 0 and nums[i] == nums[i-1]:
    #         continue
    #     while left < right:
    #         two_sum =  -(nums[left] + nums[right])
    #         if target == two_sum:
    #             answer.append([nums[i] , nums[left], nums[right]])

    #             while left<right and nums[right] == nums[right-1]:
    #                 right-=1

    #             while left < right and nums[left] == nums[left+1]:
    #                 left+=1
    #             left+=1
    #             right-=1
    #         elif target < two_sum:
    #             # print(right)
    #             left+=1
    #         elif target > two_sum:
    #             # print(left)
    #             right-=1
    # return answer
            # print(left ,right)

# Test cases
def run_tests():
    test_cases = [
        {
            "nums": [-1, 0, 1, 2, -1, -4],
            "expected": [[-1, -1, 2], [-1, 0, 1]]
        },
        {
            "nums": [0, 0, 0, 0],
            "expected": [[0, 0, 0]]
        },
        {
            "nums": [-2, 0, 1, 1, 2],
            "expected": [[-2, 0, 2], [-2, 1, 1]]
        },
        {
            "nums": [-4, -1, -1, 0, 1, 2, 3, -5, -4],
            "expected": [[-4, -1, 3], [-4, 0, 2], [-1, -1, 2], [-1, 0, 1]]
        },
        {
            "nums": [0],
            "expected": []
        }
    ]
    
    for i, test in enumerate(test_cases):
        result = threeSum(test["nums"])
        # Sort both for comparison (order doesn't matter)
        result_sorted = sorted([sorted(triplet) for triplet in result])
        expected_sorted = sorted([sorted(triplet) for triplet in test["expected"]])
        
        passed = result_sorted == expected_sorted
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"Test {i+1}: {status}")
        if not passed:
            print(f"  Input: {test['nums']}")
            print(f"  Expected: {expected_sorted}")
            print(f"  Got: {result_sorted}")

# Run all tests
run_tests()