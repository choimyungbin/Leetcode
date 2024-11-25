class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest = prices[0]
        for i in range(1, len(prices)):
            if (prices[i] - lowest) > res:
                res = prices[i] - lowest
            else:
                lowest = min(lowest, prices[i])
        
        return res