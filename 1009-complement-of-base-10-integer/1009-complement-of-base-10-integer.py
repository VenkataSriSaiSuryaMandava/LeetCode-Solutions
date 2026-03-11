class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
            
        res = 0
        i = 0
        
        while n:
            bit = (n & 1) ^ 1
            n = n >> 1

            res = res | (bit << i)
            i += 1

        return res