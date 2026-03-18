class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0
        
        def dfs(i, cur):
            if i >= len(nums):
                self.res += cur
                return
            
            cur = cur ^ nums[i]
            dfs(i + 1, cur)

            cur = cur ^ nums[i]
            dfs(i + 1, cur)
        
        dfs(0, 0)

        return self.res