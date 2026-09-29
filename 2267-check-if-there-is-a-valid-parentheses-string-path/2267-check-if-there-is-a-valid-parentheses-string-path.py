class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        total_len = m + n - 1

        if total_len % 2 != 0 or grid[0][0] == ")" or grid[m - 1][n - 1] == "(":
            return False

        max_open = total_len // 2
        visited = [[set() for _ in range(n)] for _ in range(m)]

        queue = [(0, 0, 1)]
        visited[0][0].add(1)

        for r, c, bal in queue:
            if r == m - 1 and c == n - 1:
                if bal == 0:
                    return True
                continue

            remaining = (m - 1 - r) + (n - 1 - c)
            if bal > remaining:
                continue

            for nr, nc in ((r + 1, c), (r, c + 1)):
                if nr < m and nc < n:
                    nbal = bal + (1 if grid[nr][nc] == "(" else -1)
                    if 0 <= nbal <= max_open and nbal not in visited[nr][nc]:
                        visited[nr][nc].add(nbal)
                        queue.append((nr, nc, nbal))

        return False