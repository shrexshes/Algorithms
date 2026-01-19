from typing import List
def maxProfit(prices:List[int])->int:
    '''
    Example 1:

    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
    '''
    l,r=0,1 #l=buy r=sell
    maxP=0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit=prices[r] - prices[l]
            maxP=max(maxP,profit)
        else:
            l=r
        r += 1
    print(maxP)
    return maxP

maxProfit([7,1,5,3,6,4])
