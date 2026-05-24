class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        length = len(arr)
        dp = [1] * length

        def dfs(i):
            if dp[i] != 1:
                return dp[i]
            
            for j in range(i - 1, -1, -1):
                if (i - j) > d or arr[j] >= arr[i]:
                    break
                
                dp[i] = max(dp[i], 1 + dfs(j))
            
            for j in range(i + 1, length):
                if (j - i) > d or arr[j] >= arr[i]:
                    break
                
                dp[i] = max(dp[i], 1 + dfs(j))

            return dp[i]
        
        return max(dfs(i) for i in range(length))