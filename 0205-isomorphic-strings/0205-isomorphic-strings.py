class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        count1, count2 = 0,0
        s1, t1 = '',''
        # hashMap
        hashMap1 = {}
        hashMap2 = {}
        for i,c in enumerate(s):
            if c not in hashMap1:
                hashMap1[c] = str(count1)+" "
                count1 += 1
            s1 += hashMap1[c]
        
        for i,c in enumerate(t):
            if c not in hashMap2:
                hashMap2[c] = str(count2)+" "
                count2 += 1
            t1 += hashMap2[c]
        print(s1, t1)
        return s1 == t1