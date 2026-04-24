class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        fresh = 0
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
        
        while queue and fresh > 0:
            for i in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    r = dr + row
                    c = dc + col

                    if (r < 0 or c < 0 or
                        r == rows or c == cols or
                        grid[r][c] != 1):
                        continue
                    
                    grid[r][c] = 2
                    queue.append((r, c))
                    fresh -= 1
            
            time += 1
    
        return time if fresh == 0 else -1