class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        rows = len(matrix)
        cols = len(matrix[0])

        dp = {}
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, prev):
            if (r < 0 or c < 0 or 
                r == rows or c == cols or
                matrix[r][c] <= prev):
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            maxPath = 1

            for dr, dc in directions:
                row = r + dr
                col = c + dc

                maxPath = max(maxPath, 1 + dfs(row, col, matrix[r][c]))
            
            dp[(r, c)] = maxPath
            return maxPath
        
        res = 0

        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c, -1))
        
        return res