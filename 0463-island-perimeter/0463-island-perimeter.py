class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r == rows or c == cols or
                grid[r][c] == 0):
                return 1
            
            if (r, c) in visited:
                return 0
            
            visited.add((r, c))
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