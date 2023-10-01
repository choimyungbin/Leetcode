class Solution:
    def reverseWords(self, s: str) -> str:
        tokenS = s.split()
        for i, word in enumerate(tokenS):
            newString = ""
            for j in range(len(word)-1,-1,-1):
                newString+=word[j]
            tokenS[i] = newString
        return " ".join(tokenS)