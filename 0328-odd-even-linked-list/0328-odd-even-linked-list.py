# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_dummy = ListNode()
        even_dummy = ListNode()

        odd = odd_dummy
        even = even_dummy
        cur = head

        while cur:
            odd.next = cur
            odd = odd.next
            cur = cur.next
            if cur:
                even.next = cur
                even = even.next
                cur = cur.next
        
        even.next = None
        odd.next = even_dummy.next

        return odd_dummy.next

        