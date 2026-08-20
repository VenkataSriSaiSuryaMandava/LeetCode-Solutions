class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i, curSum):
            if curSum == target:
                res.append(subset.copy())
                return
            
            if i == len(candidates) or curSum > target:
                return
            
            subset.append(candidates[i])
            backtrack(i, curSum + candidates[i])

            subset.pop()
            backtrack(i + 1, curSum)
        
        backtrack(0, 0)

        return res