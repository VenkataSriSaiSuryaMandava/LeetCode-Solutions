class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        subset = []

        def backtrack(i, curSum):
            if target == curSum:
                res.append(subset[ : : ])
                return 
            
            if curSum > target or i == len(candidates):
                return
            
            subset.append(candidates[i])
            backtrack(i, curSum + candidates[i])

            subset.pop()
            backtrack(i + 1, curSum)
        
        backtrack(0, 0)

        return res