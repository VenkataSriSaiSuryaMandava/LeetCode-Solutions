class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            if i == 0:
                return False

            j = 1

            while j * j <= i:
                if not dfs(i - j * j):
                    dp[i] = True
                    return True
                j += 1
            
            dp[i] = False
            return False
        
        return dfs(n)