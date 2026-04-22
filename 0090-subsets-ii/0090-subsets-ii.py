class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                res.append(subset[ : : ])
                return

            subset.append(nums[i])
            backtrack(i + 1)

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            subset.pop()
            backtrack(i + 1)
        
        backtrack(0)

        return res