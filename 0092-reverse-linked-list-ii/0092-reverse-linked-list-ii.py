# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        
        cur = dummy
        for i in range(left - 1):
            cur = cur.next
        
        leftPrev = cur
        leftCur = cur.next

        cur = dummy
        for i in range(right):
            cur = cur.next
        
        rightCur = cur
        rightNext = cur.next

        prev = rightNext
        cur = leftCur

        while cur != rightNext:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        leftPrev.next = prev

        return dummy.next