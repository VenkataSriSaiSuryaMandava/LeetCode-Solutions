class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = max(piles)

        while l <= r:
            m = (l + r) // 2
            count = 0
            for p in piles:
                count += math.ceil(p / m)
            if count <= h:
                res = min(m, res)
                r = m - 1
            else:
                l = m + 1
        return res