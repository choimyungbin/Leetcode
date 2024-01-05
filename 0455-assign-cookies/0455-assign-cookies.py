class Solution(object):
    def findContentChildren(self, g, s):
        if not s:
            return 0
        
        g.sort()
        s.sort()
        child, cookie = 0,0
        res = 0
        
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                res += 1
                child += 1
                cookie += 1
            else:
                cookie += 1
                
        return res