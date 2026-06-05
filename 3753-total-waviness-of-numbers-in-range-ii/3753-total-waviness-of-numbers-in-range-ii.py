from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        return self.solve(num2) - self.solve(num1 - 1)

    def solve(self, n: int) -> int:
        if n <= 0:
            return 0

        digits = list(map(int, str(n)))
        m = len(digits)

        @lru_cache(None)
        def dp(pos, tight, started, length, prev2, prev1):
            if pos == m:
                return (1, 0) if started else (0, 0)

            limit = digits[pos] if tight else 9

            total_count = 0
            total_wavy = 0

            for d in range(limit + 1):
                ntight = tight and d == limit

                if not started and d == 0:
                    cnt, wav = dp(pos + 1, ntight, False, 0, -1, -1)
                    total_count += cnt
                    total_wavy += wav
                    continue

                add = 0

                if length >= 2:
                    if (prev1 > prev2 and prev1 > d) or (prev1 < prev2 and prev1 < d):
                        add = 1

                cnt, wav = dp(pos + 1, ntight, True, length + 1, prev1, d)

                total_count += cnt
                total_wavy += wav + add * cnt

            return total_count, total_wavy

        return dp(0, True, False, 0, -1, -1)[1]