class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        for i, ticket in enumerate(tickets):
            queue.append([i, ticket])

        res = 0

        while queue:
            idx, ticket = queue.popleft()
            res += 1
            
            if ticket - 1 > 0:
                queue.append([idx, ticket - 1])

            if ticket - 1 == 0 and idx == k:
                return res