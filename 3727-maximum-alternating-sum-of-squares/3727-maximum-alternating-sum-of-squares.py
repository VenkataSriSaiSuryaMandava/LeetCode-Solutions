class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = sorted([num * num for num in nums])
        
        n = len(nums)
        k = n // 2

        return sum(nums[k : ]) - sum(nums[ : k])