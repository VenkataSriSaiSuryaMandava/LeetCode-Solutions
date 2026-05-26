class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [0] * (n + 2)

        for row in matrix:
            newDp = [float("inf")] * (n + 2)

            for i, num in enumerate(row):
                newDp[i + 1] = num + min(dp[i], dp[i + 1], dp[i + 2])
            
            dp = newDp
        
        return min(dp)