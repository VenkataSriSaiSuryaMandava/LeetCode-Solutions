class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set([(0, 0)])
        heap = [[grid[0][0], 0, 0]]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while heap:
            t, r, c = heapq.heappop(heap)

            if r == c == n - 1:
                return t
            
            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if (row < 0 or col < 0 or
                    row == n or col == n or
                    (row, col) in visited):
                    continue
                
                visited.add((row, col))
                heapq.heappush(heap, [max(t, grid[row][col]), row, col])