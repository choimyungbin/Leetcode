class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for word in strs:
                if i >= len(word) or word[i] != c:
                    return common
            common += c
        
        return common