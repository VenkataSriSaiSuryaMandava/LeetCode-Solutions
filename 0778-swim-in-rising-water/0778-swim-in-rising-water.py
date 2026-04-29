class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        visit = set((0, 0))

        minHeap = [[grid[0][0], 0, 0]]
        directions =[[1, 0], [-1, 0], [0, 1], [0, -1]]

        while minHeap:
            t, r, c = heapq.heappop(minHeap)

            if (r, c) == (n - 1, n - 1):
                return t
            
            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if (row < 0 or col < 0 or
                    row == n or col == n or 
                    (row, col) in visit):
                    continue

                visit.add((row, col))
                heapq.heappush(minHeap, [max(t, grid[row][col]), row, col])