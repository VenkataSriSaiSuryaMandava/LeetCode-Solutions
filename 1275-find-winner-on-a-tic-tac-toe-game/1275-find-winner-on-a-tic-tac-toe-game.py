class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        n = 3
        rows = [0] * n
        cols = [0] * n

        player = 1
        d1 = 0
        d2 = 0

        for r, c in moves:
            rows[r] += player
            cols[c] += player

            if r == c:
                d1 += player
            
            if r + c == n - 1:
                d2 += player
            
            if abs(rows[r]) == n or abs(cols[c]) == n or abs(d1) == n or abs(d2) == n:
                if player == 1:
                    return "A"
                else:
                    return "B"
            
            player *= -1
        
        if len(moves) == n * n:
            return "Draw"
        else:
            return "Pending"