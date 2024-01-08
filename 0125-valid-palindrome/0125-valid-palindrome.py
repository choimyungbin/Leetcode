class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
        l, r = 0, len(s)-1
        while l < r:
            while s[l] not in alpha:
                l += 1
                if l >= len(s):
                    return True
            while s[r] not in alpha:
                r -= 1
                if r <= 0:
                    return True
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        
        return True