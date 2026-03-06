# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        pathSum = defaultdict(int)
        pathSum[0] = 1

        def dfs(node, curSum):
            if not node:
                return 0
            
            curSum += node.val
            pathCount = pathSum[curSum - targetSum]
            pathSum[curSum] += 1

            leftCount = dfs(node.left, curSum)
            rightCount = dfs(node.right, curSum)

            pathCount += leftCount + rightCount
            pathSum[curSum] -= 1

            return pathCount
        
        return dfs(root, 0)