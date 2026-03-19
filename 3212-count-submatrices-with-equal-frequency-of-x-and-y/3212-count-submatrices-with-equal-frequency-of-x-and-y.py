class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        res = 0
        dp = [[[0, 0] for j in range(cols + 1)] for i in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                topX, topY = dp[r][c + 1]
                leftX, leftY = dp[r + 1][c]
                cornerX, cornerY = dp[r][c]

                if grid[r][c] == 'X':
                    curX = 1
                    curY = 0
                elif grid[r][c] == 'Y':
                    curX = 0
                    curY = 1
                else:
                    curX = 0
                    curY = 0
                    
                dp[r + 1][c + 1] = [topX + leftX - cornerX + curX, topY + leftY - cornerY + curY]

                if dp[r + 1][c + 1][0] == dp[r + 1][c + 1][1] != 0:
                    res += 1

        return res