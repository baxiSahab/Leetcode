def minEatingSpeed(piles: list[int], h: int, l = 0 , r = None) -> int:
    if sum(piles) <= h: return 1 # base case where we can just use 1
    if len(piles) == h: return max(piles) # another base case where we have to use the max
    if r == None: r = max(piles)
    else:
        k = (l+r) // 2
        if canFinish(piles , k , h) == True: return minEatingSpeed(piles , h , l = l , r = k-1)
        else: return minEatingSpeed(piles , h , l = k+1 , r = r)

def canFinish(piles , k , h):
    hours = []
    for pile in piles:
        hours.append( -(-pile)//k )
    if sum(hours) <= h: return True
    else: return False


print(canFinish([3, 6, 7, 11], 4, 8))   # Expected: True  (hours = 1+2+2+3 = 8)
print(canFinish([3, 6, 7, 11], 3, 8))   # Expected: False (hours = 1+2+3+4 = 10)
print(canFinish([30, 11, 23, 4, 20], 30, 5))  # Expected: True  (1 hour each)
print(canFinish([30, 11, 23, 4, 20], 29, 5))  # Expected: False (pile 30 needs 2 hours)
print(canFinish([1, 1, 1, 1], 1, 4))    # Expected: True  (exactly 4 hours)
print(canFinish([1, 1, 1, 1], 1, 3))    # Expected: False (needs 4, only 3 available)


# Basic case
print(minEatingSpeed([3, 6, 7, 11], 8))   # Expected: 4

# One pile, tight hours
print(minEatingSpeed([30, 11, 23, 4, 20], 5))  # Expected: 30

# One pile, lots of time
print(minEatingSpeed([30, 11, 23, 4, 20], 6))  # Expected: 23

# Single pile
print(minEatingSpeed([1000000000], 2))          # Expected: 500000000

# Already slow enough
print(minEatingSpeed([1, 1, 1, 1], 4))          # Expected: 1