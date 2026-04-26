from collections import Counter
import heapq

def topKFrequent(nums, k):
    """
    Find the k most frequent elements in the array.
    
    Your solution goes here!
    """
    
    counted = Counter(nums)
    return [ x[0] for x in sorted(counted.items() , key = lambda x:x[1], reverse=True)[:k] ]


# Test cases
test_cases = [
    {
        "input": ([1, 1, 1, 2, 2, 3], 2),
        "expected": [1, 2],  # or [2, 1] - order doesn't matter
        "description": "Basic example - 1 appears 3 times, 2 appears 2 times, 3 appears 1 time"
    },
    {
        "input": ([1], 1),
        "expected": [1],
        "description": "Single element"
    },
    {
        "input": ([4, 1, 1, -1, -3], 2),
        "expected": [1, -1],  # or [-1, 1] - order doesn't matter
        "description": "Negative numbers - 1 appears 2 times, others appear 1 time each"
    },
    {
        "input": ([1, 2, 2, 3, 3, 3], 2),
        "expected": [2, 3],  # or [3, 2]
        "description": "Clear frequency difference"
    },
    {
        "input": ([1, 1, 1, 2, 2, 2, 3, 3, 3, 3], 3),
        "expected": [1, 2, 3],
        "description": "All elements have same frequency - return first k"
    },
]

# Run tests
print("=" * 70)
print("TOP K FREQUENT ELEMENTS - TEST SUITE")
print("=" * 70)

passed = 0
failed = 0

for i, test in enumerate(test_cases, 1):
    nums, k = test["input"]
    expected = test["expected"]
    description = test["description"]
    
    print(f"\nTest {i}: {description}")
    print(f"Input: nums = {nums}, k = {k}")
    print(f"Expected: {set(expected)} (order doesn't matter)")
    
    try:
        result = topKFrequent(nums, k)
        
        # Check if result is a list and has k elements
        if not isinstance(result, list):
            print(f"❌ FAILED: Result is not a list, got {type(result)}")
            failed += 1
            continue
        
        if len(result) != k:
            print(f"❌ FAILED: Expected {k} elements, got {len(result)}")
            failed += 1
            continue
        
        # Check if result contains the correct elements (order doesn't matter)
        if set(result) == set(expected):
            print(f"✅ PASSED: Got {result}")
            passed += 1
        else:
            print(f"❌ FAILED: Got {result}")
            failed += 1
            
    except Exception as e:
        print(f"❌ ERROR: {type(e).__name__}: {e}")
        failed += 1

print("\n" + "=" * 70)
print(f"Results: {passed} passed, {failed} failed out of {len(test_cases)} tests")
print("=" * 70)