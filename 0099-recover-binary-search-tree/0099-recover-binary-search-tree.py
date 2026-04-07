# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        def dfs(node):
            if not node:
                return 

            dfs(node.left)

            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            
            self.prev = node

            dfs(node.right)
        
        self.first = None
        self.second = None
        self.prev = None

        dfs(root)

        self.first.val, self.second.val = self.second.val, self.first.val