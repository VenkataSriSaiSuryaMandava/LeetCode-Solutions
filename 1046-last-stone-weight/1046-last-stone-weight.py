class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = []
        for stone in stones:
            heapq.heappush(minHeap, -1 * stone)

        while len(minHeap) > 1:
            x = heapq.heappop(minHeap)
            y = heapq.heappop(minHeap)

            if x != y:
                heapq.heappush(minHeap, x - y)
        
        if minHeap:
            return -1 * heapq.heappop(minHeap)
        else:
            return 0
