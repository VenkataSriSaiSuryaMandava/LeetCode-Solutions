class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = {0 : 1}

        for target in range(1, target + 1):
            dp[target] = 0

            for n in nums:
                dp[target] += dp.get(target - n, 0)
        
        return dp[target]