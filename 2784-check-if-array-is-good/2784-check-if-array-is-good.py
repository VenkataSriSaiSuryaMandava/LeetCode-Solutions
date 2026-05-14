class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        maxNum = nums[-1]

        if len(nums) != maxNum + 1:
            return False
            
        for i in range(1, maxNum + 1):
            if i != nums[i - 1]:
                return False
        
        return nums[-2] == maxNum and nums[-1] == maxNum