# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if node.right and node.val < low:
                return dfs(node.right)
            if node.left and node.val > high:
                return dfs(node.left)
            
            if (node.val < low or node.val > high):
                return 0
            
            res = node.val
            if node.left:
                res += dfs(node.left)
            if node.right:
                res += dfs(node.right)
            return res
        
        
        return dfs(root)
        