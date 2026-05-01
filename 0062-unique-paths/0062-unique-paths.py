class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1] * n

        for i in range(m - 1):
            newDP = [1] * n

            for j in range(n - 2, -1, -1):
                newDP[j] = dp[j] + newDP[j + 1]

            dp = newDP
        
        return dp[0]