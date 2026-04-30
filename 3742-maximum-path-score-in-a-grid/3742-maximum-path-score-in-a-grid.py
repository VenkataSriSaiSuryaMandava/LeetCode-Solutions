class Solution(object):
    def maxPathScore(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        dp = [[-1] * (k + 1) for _ in range(n)]
        dp[0][0] = 0

        for i in range(m):
            newDp = [[-1] * (k + 1) for _ in range(n)]

            for j in range(n):
                cost = 0 if grid[i][j] == 0 else 1
                score = grid[i][j]

                for c in range(k + 1):
                    if c < cost:
                        continue
                    
                    if i > 0 and dp[j][c - cost] != -1:
                        newDp[j][c] = max(newDp[j][c], dp[j][c - cost] + score)
                    
                    if j > 0 and newDp[j - 1][c - cost] != -1:
                        newDp[j][c] = max(newDp[j][c], newDp[j - 1][c - cost] + score)
                    
                
                    if i == 0 and j == 0 and c == 0:
                        newDp[j][c] = 0
            
            dp = newDp
        
        res = max(dp[n - 1])

        return res if res != -1 else -1