class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set((0, 0))
        minHeap = [[grid[0][0], 0, 0]]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while minHeap:
            t, r, c = heapq.heappop(minHeap)

            if r == n - 1 and c == n - 1:
                return t
            
            for dr, dc in directions:
                neiR = r + dr
                neiC = c + dc

                if (neiR < 0 or neiC < 0 or
                    neiR >= n or neiC >= n or
                    (neiR, neiC) in visit):
                    continue
                
                visit.add((neiR, neiC))
                heapq.heappush(minHeap, [max(t, grid[neiR][neiC]), neiR, neiC])