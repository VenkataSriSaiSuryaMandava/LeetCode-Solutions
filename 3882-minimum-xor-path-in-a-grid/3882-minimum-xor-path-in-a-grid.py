class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [set() for _ in range(n)]
        dp[0].add(grid[0][0])

        for i in range(m):
            newdp = [set() for _ in range(n)]

            for j in range(n):
                val = grid[i][j]

                if i == 0 and j == 0:
                    newdp[j].add(val)
                    continue
                    
                if i > 0:
                    for x in dp[j]:
                        newdp[j].add(x ^ val)

                if j > 0:
                    for x in newdp[j - 1]:
                        newdp[j].add(x ^ val)

            dp = newdp

        return min(dp[n - 1])