class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        MOD = 10**9 + 7
        n = len(board)
        
        dp_score = [[0] * n for _ in range(n)]
        dp_count = [[0] * n for _ in range(n)]
        
        dp_count[n-1][n-1] = 1
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if (i == n - 1 and j == n - 1) or board[i][j] == 'X':
                    continue
                
                max_s = -1
                paths = 0
                
                directions = [(i + 1, j), (i, j + 1), (i + 1, j + 1)]
                
                for ni, nj in directions:
                    if ni < n and nj < n and dp_count[ni][nj] > 0:
                        if dp_score[ni][nj] > max_s:
                            max_s = dp_score[ni][nj]
                            paths = dp_count[ni][nj]
                        elif dp_score[ni][nj] == max_s:
                            paths = (paths + dp_count[ni][nj]) % MOD
                
                if max_s != -1:
                    current_val = int(board[i][j]) if board[i][j] not in ('E', 'S') else 0
                    dp_score[i][j] = max_s + current_val
                    dp_count[i][j] = paths

        return [dp_score[0][0], dp_count[0][0]]