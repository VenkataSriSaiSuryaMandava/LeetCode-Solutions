class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = float("inf")

        for n in nums:
            total = 0

            while n:
                total += n % 10
                n = n // 10
            
            res = min(res, total)
    
        return res