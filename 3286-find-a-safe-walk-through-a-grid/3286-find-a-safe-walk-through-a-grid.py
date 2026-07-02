class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        dist = [[float("inf") for j in range(cols)] for i in range(rows)]
        dist[0][0] = grid[0][0]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque([(0, 0)])

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if (0 <= row < rows and 
                    0 <= col < cols and 
                    dist[r][c] + grid[row][col] < dist[row][col]):
                    dist[row][col] = dist[r][c] + grid[row][col]
                    queue.append((row, col))
        
        return True if health - dist[rows - 1][cols - 1] >= 1 else False