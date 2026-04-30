class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        robleft = self.helper(nums[ : -1])
        robright = self.helper(nums[1 : ])

        return max(nums[0], robleft, robright)
    
    def helper(self, nums):
        rob1 = 0
        rob2 = 0

        for n in nums:
            temp = max(rob2, n + rob1)
            rob1 = rob2
            rob2 = temp
        
        return rob2