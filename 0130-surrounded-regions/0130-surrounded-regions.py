class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        directions = [[1, 0], [-1, 0],[0, 1], [0, -1]]

        def dfs(r, c):
            if (r < 0 or c < 0 or 
                r == rows or c == cols or
                board[r][c] != "O"):
                return

            board[r][c] = "T"

            for dr, dc in directions:
                row = r + dr
                col = c + dc

                dfs(row, col)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows - 1] or c in [0, cols - 1]):
                    dfs(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"