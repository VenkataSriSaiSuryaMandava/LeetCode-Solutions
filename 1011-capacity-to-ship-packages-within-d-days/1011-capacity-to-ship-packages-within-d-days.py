class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r

        def canShip(cap):
            ships = 1
            curCap = cap

            for w in weights:
                if curCap - w < 0:
                    curCap = cap
                    ships += 1
                curCap -= w
            
            return ships <= days

        while l <= r:
            cap = (l + r) // 2

            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        
        return res