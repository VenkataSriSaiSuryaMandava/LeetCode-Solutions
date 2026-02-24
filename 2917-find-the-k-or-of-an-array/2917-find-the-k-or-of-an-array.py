class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        res = 0

        for i in range(32):
            count = 0

            for n in nums:
                if (n >> i) & 1:
                    count += 1
                
            if count >= k:
                res = res | 1 << i
        
        return res