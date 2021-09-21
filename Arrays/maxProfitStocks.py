# Best time to buy and sell stock

# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # inputs [7,1,5,3,6,4]
        profit = 0
        j = 0
        for i in range(1,len(prices)):
            if prices[j] > prices[i]:
                j+=1
            elif prices[j] == prices[i]:
                j+=1
            else:
                profit = profit + (prices[i] - prices[j])
        return profit
