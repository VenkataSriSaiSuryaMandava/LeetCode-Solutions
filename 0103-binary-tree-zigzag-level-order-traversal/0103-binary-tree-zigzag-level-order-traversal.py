# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque([root])
        level = 0
        while queue:
            cur = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    cur.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level % 2:
                cur.reverse()
            if cur:
                res.append(cur)
            level += 1
        return res