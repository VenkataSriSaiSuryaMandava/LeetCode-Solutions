class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        res = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                index = (i * n + j + k) % (m * n)

                x = index // n
                y = index % n

                res[x][y] = grid[i][j]
        
        return res