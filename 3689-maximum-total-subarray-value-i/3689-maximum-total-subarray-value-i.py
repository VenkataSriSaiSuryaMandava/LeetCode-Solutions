class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        min_val = min(nums)

        total = max_val - min_val
        
        return total * k