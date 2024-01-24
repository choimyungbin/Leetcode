# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        numMap = {root.val:1}
        def dfs(node):
            # base case
            if not node.left and not node.right:
                temp = 0
                for n in numMap.keys():
                    if numMap[n] % 2 == 1 and not temp:
                        temp += 1
                    elif numMap[n] % 2 == 1 and temp:
                        return 0
                return 1
            
            # backtrack
            res = 0
            if node.left:
                numMap[node.left.val] = 1 + numMap.get(node.left.val, 0)
                res += dfs(node.left)
                numMap[node.left.val] -= 1
            if node.right:
                numMap[node.right.val] = 1 + numMap.get(node.right.val, 0)
                res += dfs(node.right)
                numMap[node.right.val] -= 1
            
            return res
        
        return dfs(root)