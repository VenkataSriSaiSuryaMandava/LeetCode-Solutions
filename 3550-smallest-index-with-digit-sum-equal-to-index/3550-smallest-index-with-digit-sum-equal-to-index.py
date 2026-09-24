class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            total = 0

            while num:
                total += num % 10
                num = num // 10
            
            if total == i:
                return i
        
        return -1