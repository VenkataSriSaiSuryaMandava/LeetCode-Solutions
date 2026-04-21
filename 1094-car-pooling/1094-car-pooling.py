class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        trips.sort(key = lambda t : t[1])

        curPass = 0
        minHeap = []

        for trip in trips:
            numPass, start, end = trip

            while minHeap and minHeap[0][0] <= start:
                prevEnd, prevPass = heapq.heappop(minHeap)
                curPass -= prevPass
            
            curPass += numPass

            if curPass > capacity:
                return False
            
            heapq.heappush(minHeap, (end, numPass))
        
        return True