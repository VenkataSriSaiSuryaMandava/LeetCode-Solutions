class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prevHeight):
            if (r < 0 or c < 0 or
                r == rows or c == cols or
                (r, c) in visited or 
                heights[r][c] < prevHeight):
                return
            
            visited.add((r, c))

            for dr, dc in directions:
                row = r + dr
                col = c + dc
                dfs(row, col, visited, heights[r][c])
        
        for r in range(rows):
            dfs(r, 0, pacific, -1)
            dfs(r, cols - 1, atlantic, -1)
        
        for c in range(cols):
            dfs(0, c, pacific, -1)
            dfs(rows - 1, c, atlantic, -1)
        
        res = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        
        return res