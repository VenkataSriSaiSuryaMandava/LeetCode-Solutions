class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        time = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if (row < 0 or col < 0 or
                        row == rows or col == cols or
                        grid[row][col] != 1):
                        continue
                    
                    queue.append((row, col))
                    grid[row][col] = 2
            
            time += 1
        
        return time if fresh == 0 else -1