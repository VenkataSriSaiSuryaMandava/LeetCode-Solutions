class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def backtrack(r, c, i):
            if i == len(word):
                return True
            
            if (r < 0 or c < 0 or
                r == rows or c == cols or
                board[r][c] != word[i] or
                (r, c) in visited):
                return False

            visited.add((r, c))

            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if backtrack(row, col, i + 1):
                    return True
            
            visited.remove((r, c))
            return False
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        
        return False