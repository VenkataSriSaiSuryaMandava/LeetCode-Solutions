# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.findkth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next

            prev = groupNext
            cur = groupPrev.next

            while cur != groupNext:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            temp = groupPrev.next
            groupPrev.next =kth
            groupPrev = temp
        
        return dummy.next
    
    def findkth(self, cur, k):
        while cur and k:
            cur = cur.next
            k -= 1
        
        return cur