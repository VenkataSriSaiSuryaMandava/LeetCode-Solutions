class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = nums[0]
        curSum = 0

        for num in nums:
            curSum = max(num, num + curSum)
            res = max(res, curSum)
        
        return res