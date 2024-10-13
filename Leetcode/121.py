def maxProfit(prices):
    left = 0
    maxProfit = 0

    if len(prices) <= 1:
        return 0
    
    for right in range(1, len(prices)):
        if prices[left] < prices[right]:
            maxProfit = max(maxProfit, prices[right] - prices[left])
        else:
            left = right
        
    return maxProfit


print(maxProfit([7,1,5,3,6,4]))