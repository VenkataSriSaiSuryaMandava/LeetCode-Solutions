class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                diff = nums[i] - nums[i + 1]
                res += diff

        return res