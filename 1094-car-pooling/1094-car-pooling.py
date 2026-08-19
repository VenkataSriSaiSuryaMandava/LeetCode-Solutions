class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t : t[1])

        curPass = 0
        minHeap = []

        for numPass, start, end in trips:
            while minHeap and minHeap[0][0] <= start:
                prevEnd, prevPass = heapq.heappop(minHeap)
                curPass -= prevPass
            
            curPass += numPass

            if curPass > capacity:
                return False
            
            heapq.heappush(minHeap, (end, numPass))
        
        return True