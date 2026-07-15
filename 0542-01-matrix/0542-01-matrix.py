class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        visited = set()
        queue = deque()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if 0 <= row < rows and 0 <= col < cols and (row, col) not in visited:
                    mat[row][col] = mat[r][c] + 1
                    visited.add((row, col))
                    queue.append((row, col))
        
        return mat