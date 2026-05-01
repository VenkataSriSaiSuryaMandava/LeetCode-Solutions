class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = sum(nums)

        f = sum(i * n for i, n in enumerate(nums))
        res = f

        for i in range(1, n):
            f = f + s - n * nums[n - i]
            res = max(res, f)
        
        return res
