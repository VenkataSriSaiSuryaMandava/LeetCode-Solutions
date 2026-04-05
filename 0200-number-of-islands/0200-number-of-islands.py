class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        visit = set() 
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            if (r < 0 or c < 0 or
                r == rows or c == cols or
                (r, c) in visit or
                grid[r][c] == '0'):
                return
            
            visit.add((r, c))

            for dr, dc in directions:
                row = r + dr
                col = c + dc
                bfs(row, col)
        
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    res += 1
        
        return res