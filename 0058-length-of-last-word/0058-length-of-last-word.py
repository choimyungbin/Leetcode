class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastword = s.strip().split(' ')[-1]
        return len(lastword)