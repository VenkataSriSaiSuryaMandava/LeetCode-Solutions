class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles)

        while l <= r:
            m = (l + r) // 2
            count = 0

            for p in piles:
                count += p // m
            
            if count >= h:
                l = m + 1
            else:
                r = m - 1
        
        return l