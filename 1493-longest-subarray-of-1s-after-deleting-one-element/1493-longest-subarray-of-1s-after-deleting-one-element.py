class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = 0
        res = 0
        
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                count += 1

            while (r - l + 1) - count > 1:
                if nums[l]:
                    count -= 1
                l += 1
            
            res = max(res, r - l)

        return res