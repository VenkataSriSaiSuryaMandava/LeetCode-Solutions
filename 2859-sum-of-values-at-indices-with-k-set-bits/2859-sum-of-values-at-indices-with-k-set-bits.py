class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res = 0

        for n, num in enumerate(nums):
            count = 0

            while n:
                if n & 1:
                    count += 1
                n = n >> 1
            
            if count == k:
                res += num
        
        return res