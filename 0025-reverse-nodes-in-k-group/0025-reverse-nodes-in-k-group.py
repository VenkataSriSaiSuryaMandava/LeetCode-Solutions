# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.findKth(groupPrev, k)

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
            groupPrev.next = kth
            groupPrev = temp
        
        return dummy.next
    
    def findKth(self, cur, k):
        while cur and k:
            cur = cur.next
            k -= 1
        
        return cur