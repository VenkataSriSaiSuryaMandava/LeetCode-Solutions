class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        cache = {}

        def dfs(l, r):
            if l > r:
                return 0
            
            if (l, r) in cache:
                return cache[(l, r)]
            
            cache[(l, r)] = max(nums[l] - dfs(l + 1, r), nums[r] - dfs(l, r - 1))
            
            return cache[(l, r)]
        
        return dfs(0, len(nums) - 1) >= 0