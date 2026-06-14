# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        cur = slow

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        ptr1 = head
        ptr2 = prev
        res = 0

        while ptr1 and ptr2:
            res = max(res, ptr1.val + ptr2.val)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return res