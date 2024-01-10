# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        result = 0

        def dfs(node, start):
            if node == None:
                return 0

            leftDepth = dfs(node.left, start)
            rightDepth = dfs(node.right, start)

            if node.val == start:
                Solution.result = max(leftDepth, rightDepth)
                return -1
            
            elif leftDepth >= 0 and rightDepth >= 0:
                return max(leftDepth, rightDepth)+1
            
            Solution.result = max(Solution.result, abs(leftDepth - rightDepth))
            return min(leftDepth, rightDepth) - 1

        dfs(root, start)
        return Solution.result