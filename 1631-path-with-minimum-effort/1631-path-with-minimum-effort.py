class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        minHeap = [[0, 0, 0]]
        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r, c) == (rows - 1, cols - 1):
                return diff

            if (r, c) in visit:
                continue
            visit.add((r,c))
            
            for dr, dc in directions:
                newR = r + dr
                newC = c + dc

                if (newR < 0 or newC < 0 or 
                    newR == rows or newC == cols or 
                    (newR, newC) in visit):
                    continue
                
                newDiff = max(diff, abs(heights[newR][newC] - heights[r][c]))
                heapq.heappush(minHeap, [newDiff, newR, newC])