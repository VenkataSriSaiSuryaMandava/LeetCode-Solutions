class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r == rows or c == cols or
                grid[r][c] == 1):
                return
            
            grid[r][c] = 1

            for dr, dc in directions:
                row = r + dr
                col = c + dc
                dfs(row, col)
        
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    res += 1
                    dfs(r, c)
        
        return res