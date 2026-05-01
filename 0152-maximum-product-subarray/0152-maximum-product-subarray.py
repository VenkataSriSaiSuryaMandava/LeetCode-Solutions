class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        curMax = 1
        curMin = 1

        for n in nums:
            if n == 0:
                curMax = 1
                curMin = 1
                continue
            
            temp = curMax
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(temp * n, curMin * n, n)

            res = max(res, curMax)
        
        return res