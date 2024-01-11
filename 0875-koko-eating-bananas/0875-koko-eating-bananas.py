class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = (l+r)//2
            time = 0
            for p in piles:
                time += ceil(p/m)
            if time > h:
                l = m+1
            # ⭐️⭐️⭐️⭐️
            elif time <= h:
                res = m
                r = m-1
                
        return res
        