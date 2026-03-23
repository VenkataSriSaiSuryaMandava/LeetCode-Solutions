class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [float("-inf")] * len(stoneValue)

        def dfs(i):
            if i == len(stoneValue):
                return 0
            
            if dp[i] != float("-inf"):
                return dp[i]
            
            for j in range(i, min(i + 3, len(stoneValue))):
                dp[i] = max(dp[i], sum(stoneValue[i : j + 1]) - dfs(j + 1))

            return dp[i]
        
        res = dfs(0)

        if res > 0:
            return "Alice"
        elif res < 0:
            return "Bob"
        else:
            return "Tie"