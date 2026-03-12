class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax = 0
        globalMax = nums[0]

        curMin = 0
        globalMin = nums[0]

        curSum = 0

        for n in nums:
            curMax = max(curMax + n, n)
            globalMax = max(globalMax, curMax)

            curMin = min(curMin + n, n)
            globalMin = min(globalMin, curMin)

            curSum += n

        if globalMax < 0:
            return globalMax
        
        return max(globalMax, curSum - globalMin)