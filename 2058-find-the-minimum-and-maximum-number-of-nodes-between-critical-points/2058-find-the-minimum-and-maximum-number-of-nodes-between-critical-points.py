# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = [float("inf"), float("-inf")]
        i = 0
        first = -1
        last = -1

        while head and head.next and head.next.next:
            a = head.val
            b = head.next.val
            c = head.next.next.val

            if a < b > c or a > b < c:
                if first == -1:
                    first = i
                    last = i
                else:
                    res[0] = min(res[0], i - last)
                    last = i
                    res[1] = max(res[1], last - first)
                
            i += 1
            head = head.next
        
        return res if first != last else [-1, -1]