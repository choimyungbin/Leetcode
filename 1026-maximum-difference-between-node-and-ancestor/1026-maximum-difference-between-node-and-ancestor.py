# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, smallest, biggest):
            smallest = min(smallest, node.val)
            biggest = max(biggest, node.val)

            if not node.left and not node.right:
                return biggest-smallest
            
            if node.left and node.right:
                return max(dfs(node.left, smallest, biggest),dfs(node.right, smallest, biggest))
            elif node.left:
                return dfs(node.left, smallest, biggest)
            elif node.right:
                return dfs(node.right, smallest, biggest)
            
        return dfs(root, root.val, root.val)