def maxProfit(prices: list[int]) -> int:
    N, max_price =len(prices), 0
    buying,selling = 0,1

    while buying<N-1 and selling<=N-1:
        if prices[buying] > prices[selling]:
            buying = selling
            selling+=1
        else:
            profit = prices[selling] - prices[buying]
            max_price = max(max_price, profit)
            selling+=1
    return max_price
            

# Test cases
print(maxProfit([7, 1, 5, 3, 6, 4]))  # Expected: 5
print(maxProfit([7, 6, 4, 3, 1]))      # Expected: 0
print(maxProfit([1]))                   # Expected: 0
print(maxProfit([1, 2]))               # Expected: 1
print(maxProfit([2, 4, 1, 7]))         # Expected: 6