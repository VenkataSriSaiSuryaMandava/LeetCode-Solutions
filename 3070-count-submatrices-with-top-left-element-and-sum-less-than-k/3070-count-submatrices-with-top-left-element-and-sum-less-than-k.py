class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        res = 0
        dp = [[0] * (cols + 1) for i in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                dp[r + 1][c + 1] = dp[r][c + 1] + dp[r + 1][c] - dp[r][c] + grid[r][c]

                if dp[r + 1][c + 1] <= k:
                    res += 1
        
        return res