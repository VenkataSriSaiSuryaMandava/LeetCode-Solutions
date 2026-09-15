class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        curMax = 1
        curMin = 1
        res = max(nums)

        for n in nums:
            if n == 0:
                curMax = 1
                curMin = 1
                continue
            
            temp = curMax
            curMax = max(n, curMax * n, curMin * n)
            curMin = min(n, curMin * n, temp * n)
            res = max(res, curMax)
        
        return res