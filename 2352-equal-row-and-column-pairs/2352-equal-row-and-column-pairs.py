class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = defaultdict(int)
        res = 0

        for row in grid:
            count[tuple(row)] += 1
        
        for c in range(len(grid)):
            col = tuple(grid[r][c] for r in range(len(grid)))
            res += count[col]
        
        return res