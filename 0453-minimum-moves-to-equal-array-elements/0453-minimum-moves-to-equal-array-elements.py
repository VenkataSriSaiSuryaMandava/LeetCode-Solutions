class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minNum = min(nums)
        res = 0

        for num in nums:
            res += num - minNum
        
        return res