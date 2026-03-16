class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        dr = [[0] * (n + 2) for _ in range(m + 1)]
        dl = [[0] * (n + 2) for _ in range(m + 1)]

        for i, row in enumerate(grid, 1):
            for j, v in enumerate(row, 1):
                dr[i][j] = dr[i - 1][j - 1] + v
                dl[i][j] = dl[i - 1][j + 1] + v

        res = SortedSet()

        for i, row in enumerate(grid, 1):
            for j, val in enumerate(row, 1):
                rmax = min(i - 1, m - i, j - 1, n - j)

                res.add(val)

                for r in range(1, rmax + 1):
                    e1 = dr[i + r][j] - dr[i][j - r]
                    e2 = dr[i][j + r] - dr[i - r][j]
                    e3 = dl[i][j - r] - dl[i - r][j]
                    e4 = dl[i + r][j] - dl[i][j + r]

                    s = e1 + e2 + e3 + e4 - grid[i + r - 1][j - 1] + grid[i - r - 1][j - 1]

                    res.add(s)

                while len(res) > 3:
                    res.remove(res[0])

        return list(res)[::-1]