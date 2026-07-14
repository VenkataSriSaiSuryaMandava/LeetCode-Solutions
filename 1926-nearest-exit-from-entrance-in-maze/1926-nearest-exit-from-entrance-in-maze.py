class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'

        rows = len(maze)
        cols = len(maze[0])

        while queue:
            r, c, steps = queue.popleft()
            directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

            for row, col in directions:
                if row >= 0 and col >= 0 and row < rows and col < cols and maze[row][col] != '+':
                    if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                        return steps + 1
                    
                    queue.append((row, col, steps + 1))
                    maze[row][col] = '+'
        
        return -1