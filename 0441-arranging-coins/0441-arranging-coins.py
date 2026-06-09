class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 1
        r = n

        while l <= r:
            m = (l + r) // 2
            coins = (m * (m + 1)) // 2

            if coins > n:
                r = m - 1
            elif coins < n:
                l = m + 1
            else:
                return m
        
        return r