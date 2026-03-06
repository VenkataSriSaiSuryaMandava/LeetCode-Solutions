# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        cur = head

        while cur and cur.next:
            second = cur.next
            nextGroup = cur.next.next

            second.next = cur
            cur.next = nextGroup
            prev.next = second

            prev = cur
            cur = nextGroup
        return dummy.next