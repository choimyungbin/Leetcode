class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        if len(s)==1:
            return 1
        for r in range(1,len(s)):
            sub = set(s[l:r])
            while s[r] in sub:
                l += 1
                sub = set(s[l:r])
            res = max(res, r-l+1)
        
        return res