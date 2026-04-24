class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r == rows or c == cols or
                (r, c) in visit or 
                grid[r][c] == 0):
                return 0
            
            visit.add((r, c))
            area = 1

            for dr, dc in directions:
                row = r + dr
                col = c + dc

                area += dfs(row, col)
            
            return area
        
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (r, c) not in visit:
                    area = dfs(r, c)
                    res = max(res, area)
        
        return res