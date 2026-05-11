class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        for num in nums:
            for n in str(num):
                res.append(int(n))
        
        return res