class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        fullSentence = s1+" "+s2
        s = fullSentence.split()
        hashSet = set()
        ans = set()
        for word in s:
            if word in hashSet:
                if word in ans:
                    ans.remove(word)
            else:
                hashSet.add(word)
                ans.add(word)
        
        return ans