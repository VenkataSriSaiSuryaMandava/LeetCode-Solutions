class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def canShip(cap):
            ships = 1
            curCap = cap

            for w in weights:
                if curCap - w < 0:
                    curCap = cap
                    ships += 1

                curCap -= w

            return ships <= days        
        
        l = max(weights)
        r = sum(weights)
        res = sum(weights)

        while l <= r:
            m = (l + r) // 2

            if canShip(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res