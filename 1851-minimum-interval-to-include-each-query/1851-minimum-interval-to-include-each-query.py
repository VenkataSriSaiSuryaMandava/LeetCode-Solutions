class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        resDict = {}
        i = 0
        minHeap = []

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            if minHeap:
                resDict[q] = minHeap[0][0]
            else:
                resDict[q] = -1
        
        res = []
        for q in queries:
            res.append(resDict[q])
        
        return res