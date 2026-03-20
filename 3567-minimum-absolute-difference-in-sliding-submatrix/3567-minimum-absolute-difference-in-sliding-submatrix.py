class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        
        res = [[float("inf")] * (cols - k + 1) for i in range(rows - k + 1)]

        for r in range(rows - k + 1):
            for c in range(cols - k + 1):
                visited = set()

                for i in range(k):
                    for j in range(k):
                        visited.add(grid[r + i][c + j])
                
                visited = list(sorted(visited))

                for i in range(len(visited) - 1):
                    res[r][c] = min(res[r][c], visited[i + 1] - visited[i])

                if res[r][c] == float("inf"):
                    res[r][c] = 0
        
        return res