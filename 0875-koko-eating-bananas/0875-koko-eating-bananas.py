class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l = 1
        r = max(piles)
        res = max(piles)

        while l <= r:
            m = (l + r) // 2

            count = 0
            for p in piles:
                count += ((p + m - 1) // m)
            
            if count <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res