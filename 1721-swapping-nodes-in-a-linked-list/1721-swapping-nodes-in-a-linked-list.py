# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head

        for i in range(k - 1):
            cur = cur.next
        first = cur
        second = head

        while cur.next:
            cur = cur.next
            second = second.next
        first.val, second.val = second.val, first.val
        return head