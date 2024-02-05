class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = {}
        for c in s:
            chars[c] = 1+chars.get(c,0)
        for i,c in enumerate(s):
            if chars[c] == 1:
                return i
        return -1