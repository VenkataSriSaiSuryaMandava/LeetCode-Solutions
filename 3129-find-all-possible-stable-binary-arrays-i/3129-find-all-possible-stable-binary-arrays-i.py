class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        dp0 = [[0]*(one+1) for _ in range(zero+1)]
        dp1 = [[0]*(one+1) for _ in range(zero+1)]

        for z in range(1, min(zero, limit)+1):
            dp0[z][0] = 1

        for o in range(1, min(one, limit)+1):
            dp1[0][o] = 1

        for z in range(1, zero+1):
            for o in range(1, one+1):

                dp0[z][o] = (dp0[z-1][o] + dp1[z-1][o]) % MOD
                if z-limit-1 >= 0:
                    dp0[z][o] = (dp0[z][o] - dp1[z-limit-1][o]) % MOD

                dp1[z][o] = (dp0[z][o-1] + dp1[z][o-1]) % MOD
                if o-limit-1 >= 0:
                    dp1[z][o] = (dp1[z][o] - dp0[z][o-limit-1]) % MOD

        return (dp0[zero][one] + dp1[zero][one]) % MOD