class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0 : 1}

        for t in range(1, target + 1):
            dp[t] = 0

            for num in nums:
                dp[t] += dp.get(t - num, 0)
        
        return dp[target]