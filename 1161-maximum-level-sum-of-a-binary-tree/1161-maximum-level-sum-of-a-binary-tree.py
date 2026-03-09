# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        resSum = float('-inf')
        res = 1
        level = 1
        queue = deque([root])

        while queue:
            curSum = 0
            for i in range(len(queue)):
                node = queue.popleft()
                curSum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if curSum > resSum:
                resSum = curSum
                res = level
            
            level += 1
        
        return res
