class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        minHeap = []
        res = []

        for num in arr:
            count = 0
            n = num 

            while n:
                if n & 1:
                    count += 1
                n = n >> 1
            
            heapq.heappush(minHeap, [count, num])
        
        while minHeap:
            count, num = heapq.heappop(minHeap)
            res.append(num)
        
        return res