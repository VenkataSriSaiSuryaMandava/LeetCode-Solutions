class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r == rows or c == cols or
                grid[r][c] == 0):
                return 1
            
            if (r, c) in visit:
                return 0
            
            visit.add((r, c))
            res = 0

            for dr, dc in directions:
                row = r + dr
                col = c + dc

                res += dfs(row, col)
        
            return res
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    return dfs(r, c)