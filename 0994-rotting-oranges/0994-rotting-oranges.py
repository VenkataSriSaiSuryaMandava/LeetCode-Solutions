class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        time = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while queue and fresh > 0:
            for i in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    r = dr + row
                    c = dc + col

                    if (r < 0 or r >= rows or
                        c < 0 or c >= cols or
                        grid[r][c] != 1):
                        continue
                    grid[r][c] = 2
                    queue.append((r, c))
                    fresh -= 1
            time += 1
        
        if fresh == 0:
            return time
        else:
            return -1