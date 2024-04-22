class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        profit = 0
        
        for price in prices:
            if price <= smallest:
                smallest = price
            else:
                profit = max(profit, price - smallest)
        
        return profit