class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols =len(grid[0])

        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r == rows or c == cols or
                (r, c) in visited or
                grid[r][c] == 0):
                return
            
            visited.add((r, c))
            grid[r][c] = 0

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
        
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res += 1
        
        return res