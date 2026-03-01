class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        minHeap = []

        for n in arr:
            diff = abs(n - x)
            heapq.heappush(minHeap, (diff, n))
        
        for i in range(k):
            val = heapq.heappop(minHeap)
            res.append(val[1])
            
        res.sort()
        return res