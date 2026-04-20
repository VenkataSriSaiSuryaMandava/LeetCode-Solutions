# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        def dfs(node):
            if not node:
                return [0, 0]
            
            leftPair = dfs(node.left)
            rightPair = dfs(node.right)

            withRoot = node.val + leftPair[1] + rightPair[1]
            withoutRoot = max(leftPair) + max(rightPair)

            return [withRoot, withoutRoot]
        
        return max(dfs(root))