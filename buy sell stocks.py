def maxProfit(prices: list[int]) -> int:
    right = 1
    left=0
    p = 0
    while right < len(prices):
        sold = prices[right]-prices[left]
        if sold<0: left+=1
        else: p = max(sold, p) ;right+=1
        
    return p
    # N, max_price =len(prices), 0
    # buying,selling = 0,1

    # while buying<N-1 and selling<=N-1:
    #     if prices[buying] > prices[selling]:
    #         buying = selling
    #         selling+=1
    #     else:
    #         profit = prices[selling] - prices[buying]
    #         max_price = max(max_price, profit)
    #         selling+=1
    # return max_price
            

# Test cases
print(maxProfit([7, 1, 5, 3, 6, 4]))  # Expected: 5
print(maxProfit([7, 6, 4, 3, 1]))      # Expected: 0
print(maxProfit([1]))                   # Expected: 0
print(maxProfit([1, 2]))               # Expected: 1
print(maxProfit([2, 4, 1, 7]))         # Expected: 6