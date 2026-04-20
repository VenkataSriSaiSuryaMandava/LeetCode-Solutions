class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        minHeap = []
        for stone in stones:
            heapq.heappush(minHeap, -1 * stone) 

        while len(minHeap) > 1:
            y = -1 * heapq.heappop(minHeap)
            x = -1 * heapq.heappop(minHeap)

            if x != y:
                heapq.heappush(minHeap, -1 * (y - x))
        
        if minHeap:
            return -1 * minHeap[0]
        else:
            return 0