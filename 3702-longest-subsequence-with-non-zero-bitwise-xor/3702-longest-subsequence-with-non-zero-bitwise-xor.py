class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0
        has_non_zero = False

        for num in nums:
            xor ^= num

            if num != 0:
                has_non_zero = True
        
        if not has_non_zero:
            return 0
        
        if xor != 0:
            return len(nums)
        
        return len(nums) - 1