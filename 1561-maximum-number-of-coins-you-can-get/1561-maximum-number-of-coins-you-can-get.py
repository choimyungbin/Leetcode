class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        res = 0
        piles = sorted(piles)
        ptrL, ptrR = 0, len(piles)-1
        while ptrL < ptrR:
            me = piles[ptrR-1]
            res += me
            ptrL += 1
            ptrR -= 2
        
        return res