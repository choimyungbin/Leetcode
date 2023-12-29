class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        # 1. odd length
        for i in range(len(s)):
            res += 1
            l, r = i-1, i+1
            while l > -1 and r < len(s) and s[l] == s[r]:
                    res += 1
                    l-=1
                    r+=1
        
        # 2. even length
        for i in range(len(s)):
            l, r = i, i+1
            while l > -1 and r < len(s) and s[l] == s[r]:
                res += 1
                l-=1
                r+=1
        
        return res