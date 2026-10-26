class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        res = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or 
                r == rows or c == cols or
                (r, c) in visited or 
                grid[r][c] == 0):
                return 0
            
            visited.add((r, c))
            cur = grid[r][c]

            for dr, dc in directions:
                row = r + dr
                col = c + dc

                cur += dfs(row, col)
            
            return cur
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0 and (r, c) not in visited and dfs(r, c) % k == 0:
                    res += 1
        
        return res