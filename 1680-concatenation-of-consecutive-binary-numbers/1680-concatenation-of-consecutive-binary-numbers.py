class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        
        for i in range(1, n + 1):
            length = len(bin(i)) - 2
            res = ((res << length) | i) % MOD

        return res