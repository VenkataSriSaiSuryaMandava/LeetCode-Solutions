class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(len(nums)):
            nextDP = defaultdict(int)

            for cur, count in dp.items():
                nextDP[cur + nums[i]] += count
                nextDP[cur - nums[i]] += count
            
            dp = nextDP
        
        return dp[target]