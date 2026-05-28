class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        res = 1
        dp = [[1] * 1001 for i in range(len(nums))]

        for i in range(1, len(nums)):
            for k in range(i):
                j = nums[i] - nums[k] + 500
                dp[i][j] = max(dp[i][j], 1 + dp[k][j])
                res = max(res, dp[i][j])
        
        return res