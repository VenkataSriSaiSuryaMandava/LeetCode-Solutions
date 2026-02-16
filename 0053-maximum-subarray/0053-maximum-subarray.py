class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curMax = 0

        for n in nums:
            curMax = max(curMax + n, n)
            res = max(res, curMax)
            
        return res