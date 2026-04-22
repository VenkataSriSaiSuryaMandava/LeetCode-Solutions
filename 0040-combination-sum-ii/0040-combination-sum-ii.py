class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        subset = []
        candidates.sort()
        
        def backtrack(i, curSum):
            if curSum == target:
                res.append(subset[ : :])
                return
            
            if i == len(candidates) or curSum > target:
                return
            
            subset.append(candidates[i])
            backtrack(i + 1, curSum + candidates[i])

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            subset.pop()
            backtrack(i + 1, curSum)
        
        backtrack(0, 0)

        return res