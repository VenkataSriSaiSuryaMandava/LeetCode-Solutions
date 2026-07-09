# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(cur):
            prev = None

            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            return prev
        
        l1 = reverse(l1)
        l2 = reverse(l2)

        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                l1Val = l1.val
                l1 = l1.next
            else:
                l1Val = 0
            
            if l2:
                l2Val = l2.val
                l2 = l2.next
            else:
                l2Val = 0

            total = l1Val + l2Val + carry
            carry = total // 10

            cur.next = ListNode(total % 10)
            cur = cur.next

        return reverse(dummy.next)