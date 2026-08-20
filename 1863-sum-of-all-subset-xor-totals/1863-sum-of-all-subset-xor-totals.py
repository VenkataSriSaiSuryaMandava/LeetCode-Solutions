class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0

        def backtrack(i, xor):
            if i == len(nums):
                self.res += xor
                return 
            
            backtrack(i + 1, xor ^ nums[i])
            backtrack(i + 1, xor)
        
        backtrack(0, 0)

        return self.res