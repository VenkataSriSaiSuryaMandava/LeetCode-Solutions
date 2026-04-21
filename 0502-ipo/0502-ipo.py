class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        maxProfit = []
        minCapital = []

        for p, c in zip(profits, capital):
            minCapital.append((c, -1 * p))
        
        for i in range(k):
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, p)
            
            if not maxProfit:
                break
            
            w -= heapq.heappop(maxProfit)
        
        return w