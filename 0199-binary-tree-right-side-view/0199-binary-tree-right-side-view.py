# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque([root])

        while queue:
            lenqueue = len(queue)
            for i in range(lenqueue):
                node = queue.popleft()
                if node:
                    if i == lenqueue - 1:
                        res.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        return res
        