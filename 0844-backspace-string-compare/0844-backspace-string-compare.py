class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        slist, tlist = [], []
        for c in s:
            if c != "#":
                slist.append(c)
            elif slist:
                slist.pop()
        for c in t:
            if c != "#":
                tlist.append(c)
            elif tlist:
                tlist.pop()
        return slist == tlist