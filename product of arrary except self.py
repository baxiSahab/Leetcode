import math
def productExceptSelf(nums):
    # Your solution goes here

    za_product = []
    total = math.prod(nums)
    for i in range(len(nums)):
        number = nums[i]
        if number == 0:
            left = math.prod(nums[0:i])
            right = math.prod(nums[i+1:range(nums)])
            za_product.append(left * right)
        else: za_product.append(total / number)
    return za_product


# Test cases
def test_productExceptSelf():
    # Test case 1: Basic example
    assert productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    
    # Test case 2: With a zero
    assert productExceptSelf([2, 3, 4, 5]) == [60, 40, 30, 24]
    
    # Test case 3: Two zeros would be invalid per constraints
    assert productExceptSelf([0, 1]) == [1, 0]
    
    # Test case 4: Larger array
    assert productExceptSelf([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]

    assert productExceptSelf([0,0]) == [0,0]
    
    print("All tests passed!")

# Run tests
test_productExceptSelf()

    # za_output = []
    
    # for i in range(len(nums)):
    #     lefty = math.prod(nums[:i])
    #     righty = math.prod(nums[i+1:])

    #     prody = lefty * righty

    #     za_output.append(prody)
    #     # print(za_output, prody, lefty, righty)

    # return za_output