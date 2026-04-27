class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        rows = len(grid)
        cols = len(grid[0])

        visit = set()

        directions = {
            1 : [(0, -1), (0, 1)],
            2 : [(-1, 0), (1, 0)],
            3 : [(0, -1), (1, 0)],
            4 : [(0, 1), (1, 0)],
            5 : [(0, -1), (-1, 0)],
            6 : [(-1, 0), (0, 1)]
        }

        def dfs(r, c):
            if (r, c) == (rows - 1, cols - 1):
                return True
            
            visit.add((r, c))

            for dr, dc in directions[grid[r][c]]:
                row = r + dr
                col = c + dc

                if (row < 0 or col < 0 or
                    row == rows or col == cols or
                    (row, col) in visit):
                    continue
                
                if (-dr, -dc) in directions[grid[row][col]]:
                    if dfs(row, col):
                        return True
            
            return False

        return dfs(0, 0)