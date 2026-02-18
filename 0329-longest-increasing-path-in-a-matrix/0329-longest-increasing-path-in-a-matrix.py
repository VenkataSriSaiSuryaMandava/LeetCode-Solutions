class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = {}

        def dfs(r, c, prev):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                matrix[r][c] <= prev):
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            res = 1
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                row = r + dr
                col = c + dc
                res = max(res, 1 + dfs(row, col, matrix[r][c]))
            
            dp[(r, c)] = res
            return res

        maxPath = 0
        for r in range(rows):
            for c in range(cols):
                maxPath = max(maxPath, dfs(r, c, -1))
        
        return maxPath