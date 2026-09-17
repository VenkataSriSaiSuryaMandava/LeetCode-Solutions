class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [float("inf")] * (n + 1)
        dp[-2] = 0

        for i in range(m - 1, -1, -1):
            newDP = [float("inf")] * (n + 1)

            for j in range(n - 1, -1, -1):
                newDP[j] = grid[i][j] + min(dp[j], newDP[j + 1])
        
            dp = newDP
        
        return dp[0]