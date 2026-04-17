"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        copy = {None : None}

        cur = head
        while cur:
            copy[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            copy[cur].next = copy[cur.next]
            copy[cur].random = copy[cur.random]
            cur = cur.next
        
        return copy[head]