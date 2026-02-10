class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        visit = set()
        res = 0

        def bfs(r, c):
            queue = deque()
            visit.add((r, c))
            queue.append((r, c))
            while queue:
                row , col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if (r in range(rows) and 
                        c in range(cols) and 
                        grid[r][c] == "1" and 
                        (r, c) not in visit):
                        visit.add((r, c))
                        queue.append((r, c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    visit.add((r, c))
                    bfs(r, c)
                    res += 1
        return res