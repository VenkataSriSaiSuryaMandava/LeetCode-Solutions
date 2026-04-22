class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def backtrack(i, xorTotal):
            if i == len(nums):
                return xorTotal
            
            return backtrack(i + 1, xorTotal ^ nums[i]) + backtrack(i + 1, xorTotal)
        
        return backtrack(0, 0)