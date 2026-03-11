class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap = []
        res = 0

        for i in range(candidates):
            heapq.heappush(heap, [costs[i], i])
        front_end = i

        back_end = max(front_end + 1, len(costs) - candidates)
        for i in range(back_end, len(costs)):
            heapq.heappush(heap, [costs[i], i])
        
        while k > 0:
            cost, index = heapq.heappop(heap)
            res += cost
            k -= 1

            if front_end < back_end - 1:
                if index <= front_end:
                    front_end += 1
                    heapq.heappush(heap, [costs[front_end], front_end])
                else:
                    back_end -= 1
                    heapq.heappush(heap, [costs[back_end], back_end])
        
        return res