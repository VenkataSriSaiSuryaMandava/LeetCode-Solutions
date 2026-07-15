class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1 

        n = len(grid)
        res = 1

        queue = deque([(0, 0)])
        visited = set([(0, 0)])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if (r, c) == (n - 1, n - 1):
                    return res
                
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if (0 <= row < n and 
                        0 <= col < n and 
                        (row, col) not in visited and 
                        grid[row][col] == 0):
                        queue.append((row, col))
                        visited.add((row, col))
            
            res += 1
        
        return -1