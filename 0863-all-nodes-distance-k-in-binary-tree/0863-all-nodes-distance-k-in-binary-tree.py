# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def dfs(node, parent):
            if not node:
                return None
            
            parentChild[node] = parent
            
            dfs(node.left, node)
            dfs(node.right, node)
        
        def dfs2(node, parent, k):
            if not node:
                return 
            
            if k == 0:
                res.append(node.val)
                return 
            
            for nextNode in (node.left, node.right, parentChild[node]):
                if nextNode != parent:
                    dfs2(nextNode, node, k - 1)
        
        parentChild = {}
        dfs(root, None)

        res = []
        dfs2(target, None, k)

        return res