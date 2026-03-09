# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node, left, cur):
            if not node:
                return None
            
            self.res = max(self.res, cur)

            if left:
                dfs(node.left, True, 1)
                dfs(node.right, False, cur + 1)
            else:
                dfs(node.left, True, cur + 1)
                dfs(node.right, False, 1)
        
        dfs(root.left, True, 1)
        dfs(root.right, False, 1)

        return self.res