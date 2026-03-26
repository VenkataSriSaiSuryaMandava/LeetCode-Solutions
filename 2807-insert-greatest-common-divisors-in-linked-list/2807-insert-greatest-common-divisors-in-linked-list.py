# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if b == 0:
                return abs(a)
            
            return gcd(b, a % b)

        cur = head

        while cur and cur.next:
            nextNode = cur.next

            val = gcd(cur.val, nextNode.val)
            node = ListNode(val)

            node.next = nextNode
            cur.next = node
            cur = nextNode
        
        return head