class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        for row in range(rows):
            l = 0
            r = cols - 1
            idx = -1

            while l <= r:
                m = (l + r) // 2

                if grid[row][m] < 0:
                    idx = m
                    r = m - 1
                else:
                    l = m + 1
            
            if idx != -1:
                res += cols - idx

        return res