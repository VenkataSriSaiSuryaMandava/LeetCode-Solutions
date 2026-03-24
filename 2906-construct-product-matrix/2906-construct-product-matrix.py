class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        MOD = 12345

        res = [[1] * cols for i in range(rows)]

        prefix = 1
        for r in range(rows):
            for c in range(cols):
                res[r][c] = (res[r][c] * prefix) % MOD
                prefix = (prefix * grid[r][c]) % MOD
        
        suffix = 1
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                res[r][c] = (res[r][c] * suffix) % MOD
                suffix = (suffix * grid[r][c]) % MOD
        
        return res