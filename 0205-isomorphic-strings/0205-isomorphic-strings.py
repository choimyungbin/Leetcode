class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        tIntoS = ''
        hashMap = {}
        for i,c in enumerate(t):
            if c not in hashMap:
                if s[i] in hashMap.values():
                    return False
                hashMap[c] = s[i]
            tIntoS += hashMap[c]
        return s == tIntoS