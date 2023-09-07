class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxLength = 0
        
        def findPalindrome(l,r, res, maxLength):
            while l>=0 and r<len(s) and s[l] == s[r]:
                # base case
                if (r-l+1) > maxLength:
                    res = s[l:r+1]
                    maxLength = r-l+1

                l-=1
                r+=1
            return res, maxLength
        
        for i in range(len(s)):
            # if length is odd
            l, r = i, i
            res, maxLength = findPalindrome(l,r, res, maxLength)
            # if length is even
            l,r = i,i+1
            res, maxLength = findPalindrome(l,r, res, maxLength)
        
        return res
                
