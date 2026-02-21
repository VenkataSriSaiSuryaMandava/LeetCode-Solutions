class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res = 0
        prime = {2, 3, 5, 7, 11, 13, 17, 19}
        for n in range(left, right + 1):
            count = 0
            while n > 0:
                if n % 2:
                    count += 1
                n = n // 2

            if count in prime:
                res += 1
        
        return res
