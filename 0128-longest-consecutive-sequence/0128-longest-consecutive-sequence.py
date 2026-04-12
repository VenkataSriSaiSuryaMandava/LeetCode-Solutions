class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsSet = set(nums)
        res = 0

        for num in numsSet:
            if num - 1 not in numsSet:
                count = 0

                while num in numsSet:
                    num += 1
                    count += 1
            
                res = max(res, count)
        
        return res