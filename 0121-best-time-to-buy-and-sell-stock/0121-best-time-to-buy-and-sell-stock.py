class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        l = 0

        for r in range(1, len(prices)):
            if prices[l] >= prices[r]:
                l = r
            res = max(res, prices[r] - prices[l])
        
        return res