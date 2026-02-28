class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        m = r - l + 1

        digitSum = (l + r) * m // 2 % MOD
        repeat = pow(m, k - 1, MOD)
        geom = (pow(10, k, MOD) - 1) * pow(9, MOD - 2, MOD) % MOD

        return digitSum * repeat % MOD * geom % MOD