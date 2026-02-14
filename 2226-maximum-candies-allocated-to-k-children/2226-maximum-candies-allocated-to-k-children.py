class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l = 1
        r = max(candies)
        res = 0
        while l <= r:
            m = (l + r) // 2
            count = 0
            for c in candies:
                count += c // m
            if count >= k:
                res = max(res, m)
                l = m + 1
            else:
                r = m - 1
        return res