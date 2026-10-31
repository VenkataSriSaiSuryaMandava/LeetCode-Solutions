class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 1_000_000_007

        memo = {}

        def get_destination(r: int, c: int, direction: int):
            state = (r, c, direction)
            if state in memo:
                return memo[state]

            if not (0 <= r < m and 0 <= c < n):
                memo[state] = None
                return None

            if grid[r][c] == 0:
                memo[state] = (r, c)
                return (r, c)

            if (r, c) == (m - 1, n - 1):
                memo[state] = (r, c)
                return (r, c)

            if direction == 0:
                res = get_destination(r + 1, c, 1)
            else:
                res = get_destination(r, c + 1, 0)

            memo[state] = res
            return res

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                val = dp[r][c]
                if val == 0:
                    continue

                if c + 1 < n:
                    dest = get_destination(r, c + 1, 0)
                    if dest is not None:
                        dp[dest[0]][dest[1]] = (dp[dest[0]][dest[1]] + val) % MOD

                if r + 1 < m:
                    dest = get_destination(r + 1, c, 1)
                    if dest is not None:
                        dp[dest[0]][dest[1]] = (dp[dest[0]][dest[1]] + val) % MOD

        return dp[m - 1][n - 1]