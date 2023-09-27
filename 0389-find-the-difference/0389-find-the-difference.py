class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = 0
        # XOR
        for cs in s: 
            c ^= ord(cs)
        for ct in t: 
            c ^= ord(ct)
        return chr(c) 
        
        