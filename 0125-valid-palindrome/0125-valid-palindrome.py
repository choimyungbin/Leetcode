class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        s = s.lower()
        while l < r:
            while l<r and s[l] not in "abcdefghijklmnopqrstuvwxyz0123456789":
                l += 1
            while l<r and s[r] not in "abcdefghijklmnopqrstuvwxyz0123456789":
                r -= 1
            if l >= r:
                return True
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True