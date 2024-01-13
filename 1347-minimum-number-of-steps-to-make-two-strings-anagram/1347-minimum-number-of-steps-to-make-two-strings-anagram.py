class Solution:
    def minSteps(self, s: str, t: str) -> int:
        l1 = sorted([c for c in s])
        l2 = sorted([c for c in t])
        p1, p2 = 0,0
        res = 0
        while p1 < len(l1) and p2 < len(l1):
            if ord(l1[p1]) == ord(l2[p2]):
                p1 += 1
                p2 += 1
            elif ord(l1[p1]) > ord(l2[p2]):
                p2 += 1
            else:
                res += 1
                p1 += 1
        if p1 < len(l1):
            res += len(l1)-p1
                
        return res