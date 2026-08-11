"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeToCopy = {None : None}

        cur = head

        while cur:
            copy = Node(cur.val)
            nodeToCopy[cur] = copy
            cur = cur.next
        
        cur = head
        
        while cur:
            nodeToCopy[cur].next = nodeToCopy[cur.next]
            nodeToCopy[cur].random = nodeToCopy[cur.random]
            cur = cur.next
        
        return nodeToCopy[head]