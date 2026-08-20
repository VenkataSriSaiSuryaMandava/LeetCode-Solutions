class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []

        def backtrack(i, curSum):
            if curSum == target:
                res.append(subset.copy())
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