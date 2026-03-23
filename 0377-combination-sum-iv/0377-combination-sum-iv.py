class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}
        
        def backtrack(curSum):
            if curSum in cache:
                return cache[curSum]

            if curSum == target:
                return 1
            
            if curSum > target:
                return 0
        
            cache[curSum] = 0

            for j in range(len(nums)):
                cache[curSum] += backtrack(curSum + nums[j])

            return cache[curSum]
        
        return backtrack(0)
