class Solution:
    def minInsertions(self, s: str) -> int:
        dp = [[0 for j in range(len(s) + 1)] for i in range(len(s) + 1)]
        res = 0

        for i in range(len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                if s[i] == s[j]:
                    if i == j:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 2
                    
                    if i > 0:
                        dp[i][j] += dp[i - 1][j + 1]
                else:
                    dp[i][j] = dp[i][j + 1]

                    if i > 0:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j])
                
                res = max(res, dp[i][j])
        
        return len(s) - res