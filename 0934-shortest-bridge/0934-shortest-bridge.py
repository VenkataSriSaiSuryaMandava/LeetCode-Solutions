class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        res = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            queue.append((r, c))
            grid[r][c] = 2

            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if 0 <= row < n and 0 <= col < n and grid[row][col] == 1:
                    dfs(row, col)
        
        startRow, startCol = next((r, c) for r in range(n) for c in range(n) if grid[r][c] == 1)
        dfs(startRow, startCol)
        
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if 0 <= row < n and 0 <= col < n:
                        if grid[row][col] == 1:
                            return res
                        elif grid[row][col] == 0:
                            grid[row][col] = 2
                            queue.append((row, col))
            
            res += 1
        
        return res