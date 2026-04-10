class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        difference = {}

        for i, num in enumerate(nums):
            diff = target - num
            
            if diff in difference:
                return[i, difference[diff]]
            
            difference[num] = i