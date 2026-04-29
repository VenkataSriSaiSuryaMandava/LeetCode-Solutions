class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tempPrices = prices[ : : ]

            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                
                if prices[s] + p < tempPrices[d]:
                    tempPrices[d] = prices[s] + p
            
            prices = tempPrices
        
        if prices[dst] == float("inf"):
            return -1
        else:
            return prices[dst]