# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(node):
            if not node:
                return None
            
            leftTail = dfs(node.left)
            rightTail = dfs(node.right)

            if node.left:
                leftTail.right = node.right
                node.right = node.left
                node.left = None
            
            if rightTail:
                return rightTail
            elif leftTail:
                return leftTail
            else:
                return node
        
        dfs(root)
        