class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        curMax = 0
        globalMax = nums[0]

        curMin = 0
        globalMin = nums[0]

        curSum = 0

        for num in nums:
            curSum += num

            curMax = max(curMax + num, num)
            globalMax = max(globalMax, curMax)

            curMin = min(curMin + num, num)
            globalMin = min(globalMin, curMin)
        
        if globalMax < 0:
            return globalMax
        
        return max(globalMax, curSum - globalMin)