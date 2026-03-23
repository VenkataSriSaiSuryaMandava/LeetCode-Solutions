class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        rows = len(grid)
        cols = len(grid[0])

        dp = [[[grid[0][0], grid[0][0]] for i in range(cols)] for j in range(rows)]

        for row in range(1, rows):
            prev_prod = dp[row - 1][0][0]
            cur_val = grid[row][0]
            dp[row][0][0] = prev_prod * cur_val
            dp[row][0][1] = prev_prod * cur_val

        for col in range(1, cols):
            prev_prod = dp[0][col - 1][0]
            cur_val = grid[0][col]
            dp[0][col][0] = prev_prod * cur_val
            dp[0][col][1] = prev_prod * cur_val
        
        for r in range(1, rows):
            for c in range(1, cols):
                cur_val = grid[r][c]
                
                min_from_left = dp[r][c - 1][0]
                min_from_top = dp[r - 1][c][0]

                max_from_top = dp[r - 1][c][1]
                max_from_left = dp[r][c - 1][1]

                min_value = min(min_from_left, min_from_top) * cur_val
                max_value = max(max_from_left, max_from_top) * cur_val

                if cur_val >= 0: 
                    dp[r][c][0] = min_value
                    dp[r][c][1] = max_value
                else:
                    dp[r][c][0] = max_value
                    dp[r][c][1] = min_value

        max_product = dp[-1][-1][1]

        if max_product < 0:
            return -1
        else:
            return max_product % MOD