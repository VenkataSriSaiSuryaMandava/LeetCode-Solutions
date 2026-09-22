class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dp = {}

        def dfs(r, c, prev):
            if (r < 0 or c < 0 or
                r == rows or c == cols or
                matrix[r][c] <= prev):
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            res = 1

            for dr, dc in directions:
                row = r + dr
                col = c + dc

                res = max(res, 1 + dfs(row, col, matrix[r][c]))
            
            dp[(r, c)] = res
            return res
        
        longPath = 0

        for r in range(rows):
            for c in range(cols):
                longPath = max(longPath, dfs(r, c, -1))
        
        return longPath
            