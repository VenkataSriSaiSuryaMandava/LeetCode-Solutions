class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        res = -1

        for idx, num in enumerate(nums):
            if num != idx:
                res &= num
        
        return max(res, 0)