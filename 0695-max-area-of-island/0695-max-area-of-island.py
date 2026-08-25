class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r == rows or c == cols or
                (r, c) in visited or 
                grid[r][c] == 0):
                return 0
            
            visited.add((r, c))
            area = 1

            for dr, dc in directions:
                row = r + dr
                col = c + dc

                area += dfs(row, col)
            
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (r, c) not in visited:
                    area = dfs(r, c)
                    res = max(res, area)
        
        return res