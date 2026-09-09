# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_new = cur = ListNode(None)
        while head:
            if cur.val != head.val:
                cur.next = ListNode(head.val)
                cur = cur.next
            head = head.next
        return head_new.next


        