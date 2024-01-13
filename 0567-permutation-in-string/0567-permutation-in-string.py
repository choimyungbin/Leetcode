class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, length = 0, len(s1)
        l1, l2 = [0]*26,[0]*26
        for c in s1:
            l1[ord(c)-97]+=1
        
        for r in range(len(s2)):
            l2[ord(s2[r])-97] += 1
            if r-l+1 == length:
                if l1 == l2:
                    return True
                l2[ord(s2[l])-97] -= 1
                l += 1
        
        return False