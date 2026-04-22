class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])

        visit = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def backtrack(r, c, i):
            if i == len(word):
                return True
            
            if (r < 0 or c < 0 or
                r == rows or c == cols or
                (r, c) in visit or
                word[i] != board[r][c]):
                return False
            
            visit.add((r, c))
            
            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if backtrack(row, col, i + 1):
                    return True
            
            return False

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and backtrack(r, c, 0):
                    return True
        
        return False