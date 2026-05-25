class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for i in range(m - 1):
            newDp = [1] * n

            for j in range(n - 2, -1, -1):
                newDp[j] = newDp[j + 1] + dp[j]
            
            dp = newDp
        
        return dp[0]