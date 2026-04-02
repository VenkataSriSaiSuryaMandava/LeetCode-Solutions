class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 1

        for n in nums:
            if n == 0:
                return 0

            if n < 0:
                res *= -1
                
        return res