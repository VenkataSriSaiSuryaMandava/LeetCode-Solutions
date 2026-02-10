class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        res = 0
        visit = set()

        def bfs(r, c):
            queue = deque()
            visit.add((r, c))
            queue.append((r, c))
            area = 0

            while queue:
                row, col = queue.popleft()
                area += 1
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r = dr + row
                    c = dc + col

                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == 1 and
                        (r, c) not in visit):
                        queue.append((r, c))
                        visit.add((r, c))
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = bfs(r, c)
                    res = max(res, area)
        
        return res