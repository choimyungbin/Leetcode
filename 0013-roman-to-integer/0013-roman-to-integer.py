class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        l = 0
        for i in range(len(s)):
            if s[i] == 'M':
                res += 1000
            elif s[i] == 'D':
                res += 500
            elif s[i] == 'C':
                if i<len(s)-1 and (s[i+1] == 'M' or s[i+1] == 'D'):
                        res -= 100
                else:
                    res += 100
            elif s[i] == 'L':
                res += 50
            elif s[i] == 'X':
                if i<len(s)-1 and (s[i+1] == 'C' or s[i+1] == 'L'):
                        res -= 10
                else:
                    res += 10
            elif s[i] == 'V':
                res += 5
            elif s[i] == 'I':
                if i<len(s)-1 and (s[i+1] == 'X' or s[i+1] == 'V'):
                        res -= 1
                else:
                    res += 1
        return res