class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        hashMap = {}
        for i in range(len(s)):
            if s[i] in hashMap:
                res = max(res, i-hashMap[s[i]]-1)
            else:
                hashMap[s[i]] = i
                
        return res