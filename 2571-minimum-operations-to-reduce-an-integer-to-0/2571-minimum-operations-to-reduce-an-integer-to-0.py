class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        count = 0

        while n:
            if n & 1:
                count += 1
            elif count:
                res += 1
                count = 0 if count == 1 else 1
            
            n >>= 1
        
        res += 1 if count == 1 else 2

        return res