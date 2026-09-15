class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[True for j in range(n)] for i in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] != s[j] or not dp[i + 1][j - 1]:
                    dp[i][j] = False
        
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]
            
            if i >= n:
                return 0
            
            cache[i] = dfs(i + 1)

            for j in range(i + k - 1, n):
                if dp[i][j]:
                    cache[i] = max(cache[i], 1 + dfs(j + 1))
            
            return cache[i]
        
        return dfs(0)