class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res = 0
        prime = {2, 3, 5, 7, 11, 13, 17, 19}

        for i in range(left, right + 1):
            count = 0
            n = i

            while n > 0:
                count += n & 1
                n = n >> 1

            if count in prime:
                res += 1
        
        return res