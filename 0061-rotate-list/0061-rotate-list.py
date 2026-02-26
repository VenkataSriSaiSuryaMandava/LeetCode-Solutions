# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
            
        dummy = ListNode(0, head)
        cur = head
        count = 0

        while cur:
            cur = cur.next
            count += 1
        k = k % count

        slow = dummy
        fast = dummy

        for i in range(k):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        fast.next = dummy.next
        dummy.next = slow.next
        slow.next = None

        return dummy.next
        
