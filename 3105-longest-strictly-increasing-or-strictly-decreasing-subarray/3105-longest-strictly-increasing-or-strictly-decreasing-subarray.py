class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 0
        count = 0

        for r in range(1, len(nums)):
            if nums[r - 1] > nums[r]:
                count += 1
                res = max(res, count)
            else:
                count = 0
        
        count = 0

        for r in range(1, len(nums)):
            if nums[r - 1] < nums[r]:
                count += 1
                res = max(res, count)
            else:
                count = 0
        
        return res + 1