class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.res = 0

        def backtrack(i, xorTotal):
            if i == len(nums):
                self.res += xorTotal
                return
            
            backtrack(i + 1, xorTotal ^ nums[i])
            backtrack(i + 1, xorTotal)
        
        backtrack(0, 0)

        return self.res