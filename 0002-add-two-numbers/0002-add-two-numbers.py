# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            if l1:
                a = l1.val 
                l1 = l1.next
            else:
                a = 0
            
            if l2:
                b = l2.val
                l2 = l2.next
            else:
                b = 0
            
            add = a + b + carry
            cur.next = ListNode(add % 10)
            cur = cur.next
            carry = add // 10
        return dummy.next