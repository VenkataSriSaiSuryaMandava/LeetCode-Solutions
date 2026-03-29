# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        res = 0
        nums = set(nums)

        while head:
            while head and head.val not in nums:
                head = head.next
            
            if head is not None:
                res += 1
            
            while head and head.val in nums:
                head = head.next

        return res