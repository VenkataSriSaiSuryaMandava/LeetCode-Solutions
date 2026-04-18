# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        def dfs(node):
            if not node:
                return [0, True]
            
            leftTree = dfs(node.left)
            rightTree = dfs(node.right)

            balanced = leftTree[1] and rightTree[1] and abs(leftTree[0] - rightTree[0]) < 2

            return [1 + max(leftTree[0], rightTree[0]),  balanced]

        return dfs(root)[1]