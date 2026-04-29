class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        rows = len(heights)
        cols = len(heights[0])

        visit = set()
        minHeap = [[0, 0, 0]]

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r, c) == (rows - 1, cols - 1):
                return diff
            
            if (r, c) in visit:
                continue
            
            visit.add((r, c))

            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if (row < 0 or col < 0 or
                    row == rows or col == cols or
                    (row, col) in visit):
                    continue
                
                newDiff = max(diff, abs(heights[row][col] - heights[r][c]))
                heapq.heappush(minHeap, [newDiff, row, col])

