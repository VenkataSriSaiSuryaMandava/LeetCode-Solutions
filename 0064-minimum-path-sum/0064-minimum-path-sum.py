class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [float(inf)] * (n + 1)
        dp[-2] = 0

        for i in range(m - 1, -1, -1):
            newDp = [float(inf)] * (n + 1)

            for j in range(n - 1, -1, -1):
                newDp[j] = grid[i][j] + min(dp[j], newDp[j + 1])
            
            dp = newDp
        
        return dp[0]