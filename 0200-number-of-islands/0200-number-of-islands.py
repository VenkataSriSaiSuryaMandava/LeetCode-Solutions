class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r == rows or c == cols or
                (r, c) in visited or
                grid[r][c] == '0'):
                return 
            
            visited.add((r, c))

            for dr, dc in directions:
                row = r + dr
                col = c + dc

                dfs(row, col)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    res += 1
        
        return res