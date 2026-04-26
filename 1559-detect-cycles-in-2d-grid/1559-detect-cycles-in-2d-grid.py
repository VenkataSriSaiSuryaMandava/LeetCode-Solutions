class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        rows = len(grid)
        cols = len(grid[0])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = set()

        def dfs(r, c, rPrev, cPrev, val):
            visit.add((r, c))

            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if (row < 0 or col < 0 or
                    row == rows or col == cols or
                    val != grid[row][col] or
                    (row == rPrev and col == cPrev)):
                    continue
                
                if (row, col) in visit:
                    return True
                
                if dfs(row, col, r, c, val):
                    return True
            
            return False
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and dfs(r, c, -1, -1, grid[r][c]):
                    return True
        
        return False