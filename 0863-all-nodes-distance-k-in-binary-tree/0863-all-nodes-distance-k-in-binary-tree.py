# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def findParent(node, parent):
            if not node:
                return 
            
            childToParent[node] = parent

            findParent(node.left, node)
            findParent(node.right, node)
        
        childToParent = {}
        findParent(root, None)

        def findNodes(node, parent, k):
            if not node:
                return
            
            if k == 0:
                res.append(node.val)
                return
            
            for nextNode in (node.left, node.right, childToParent[node]):
                if nextNode != parent:
                    findNodes(nextNode, node, k - 1)
        
        res = []
        findNodes(target, None, k)

        return res