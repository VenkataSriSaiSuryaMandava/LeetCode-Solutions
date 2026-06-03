class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[[0 for k in range(n + 1)] for j in range(m + 1)] for i in range(len(strs) + 1)]

        for cur_idx, cur_str in enumerate(strs, 1):
            zero_count = cur_str.count('0')
            one_count = cur_str.count('1')

            for i in range(m + 1):
                for j in range(n + 1):
                    dp[cur_idx][i][j] = dp[cur_idx - 1][i][j]

                    if zero_count <= i and one_count <= j:
                        dp[cur_idx][i][j] = max(dp[cur_idx][i][j], 1 + dp[cur_idx - 1][i - zero_count][j - one_count])
        
        return dp[len(strs)][m][n]
                    