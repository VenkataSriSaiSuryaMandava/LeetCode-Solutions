class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        prefixSum = []
        prefix = 0

        for stone in stones:
            prefix += stone
            prefixSum.append(prefix)
        
        n = len(stones)
        dp = {}

        def dfs(i):
            if i >= n - 1:
                return prefixSum[-1]
            
            if i in dp:
                return dp[i]
            
            dp[i] = max(dfs(i + 1), prefixSum[i] - dfs(i + 1))
            return dp[i]
        
        return dfs(1)