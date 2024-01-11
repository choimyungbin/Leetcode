class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def dfs(leftLen, rightLen):
            if leftLen == rightLen == n:
                res.append("".join(stack))
                return
            if leftLen < n:
                stack.append('(')
                dfs(leftLen+1, rightLen)
                stack.pop()
            if leftLen > rightLen:
                stack.append(')')
                dfs(leftLen, rightLen+1)
                stack.pop()
            
        dfs(0, 0)
        return res