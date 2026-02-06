# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur = slow.next
        prev = None

        slow.next = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        ptr1 = head
        ptr2 = prev

        while ptr1 and ptr2:
            temp1 = ptr1.next
            ptr1.next = ptr2
            temp2 = ptr2.next
            ptr2.next = temp1
            ptr1 = temp1
            ptr2 = temp2
