# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = []
        leaf2 = []

        def dfs(node):
            if not node:
                return None
            
            dfs(node.left)
            dfs(node.right)

            if not node.left and not node.right:
                leaf1.append(node.val)
        
        dfs(root1)
        
        def dfs(node):
            if not node:
                return None
            
            dfs(node.left)
            dfs(node.right)

            if not node.left and not node.right:
                leaf2.append(node.val) 
        
        dfs(root2)

        return leaf1 == leaf2