class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        subset = []

        def backtrack(i, curSum, target):
            if target == curSum:
                res.append(subset[ : : ])
                return 
            
            if curSum > target or i == len(candidates):
                return
            
            subset.append(candidates[i])
            backtrack(i, curSum + candidates[i], target)

            subset.pop()
            backtrack(i + 1, curSum, target)
        
        backtrack(0, 0, target)

        return res