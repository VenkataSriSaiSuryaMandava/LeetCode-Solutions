class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [n] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            for s in range(1, int(target ** 0.5) + 1):
                square = s * s
                dp[target] = min(dp[target], 1 + dp[target - square])
        
        return dp[n]