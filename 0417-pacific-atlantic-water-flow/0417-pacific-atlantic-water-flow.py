class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(heights)
        cols = len(heights[0])

        res = []
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        pacific = set()
        atlantic = set()

        def dfs(r, c, visit, prev):
            if (r < 0 or c < 0 or 
                r == rows or c == cols or
                (r, c) in visit
                or heights[r][c] < prev):
                return
            
            visit.add((r, c))

            for dr, dc in directions:
                row = r + dr
                col = c + dc

                dfs(row, col, visit, heights[r][c])
        
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])
        
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        
        return res