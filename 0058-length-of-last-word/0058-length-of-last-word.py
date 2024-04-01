class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p = len(s)-1
        count = 0
        while s[p] == ' ':
            p -= 1
        while p>=0 and s[p] != ' ':
            count += 1
            p -= 1
            
        return count