# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        first = head
        second = slow.next

        slow.next = None

        ptr1 = self.sortList(first)
        ptr2 = self.sortList(second)
        return self.merge(ptr1, ptr2)

    def merge(self, ptr1, ptr2):
        dummy = ListNode()
        cur = dummy

        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                cur.next = ptr1
                ptr1 = ptr1.next
            else:
                cur.next = ptr2
                ptr2 = ptr2.next
            cur = cur.next
        
        if ptr1:
            cur.next = ptr1
        if ptr2:
            cur.next = ptr2
        
        return dummy.next