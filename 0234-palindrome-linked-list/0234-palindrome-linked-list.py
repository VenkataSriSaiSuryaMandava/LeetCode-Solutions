# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        cur = slow.next
        prev = None

        slow.next = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        first = head
        second = prev

        while first and second:
            if first.val != second.val:
                return False
            
            first = first.next
            second = second.next
        
        return True