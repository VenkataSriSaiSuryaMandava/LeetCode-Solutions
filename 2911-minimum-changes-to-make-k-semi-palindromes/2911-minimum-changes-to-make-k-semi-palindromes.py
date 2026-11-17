
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        inf = float('inf')
        cost = [[inf] * (n + 1) for _ in range(n + 1)]

        for length in range(2, n + 1):
            divisors = [d for d in range(1, length) if length % d == 0]

            for i in range(n - length + 1):
                for d in divisors:
                    changes = 0
                    group_len = length // d

                    for r in range(d):
                        for t in range(group_len // 2):
                            left = i + r + t * d
                            right = i + r + (group_len - 1 - t) * d

                            if s[left] != s[right]:
                                changes += 1

                    cost[i][i + length] = min(
                        cost[i][i + length], changes
                    )

        dp = [[inf] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for end in range(2 * parts, n + 1):
                for start in range(2 * (parts - 1), end - 1):
                    dp[parts][end] = min(
                        dp[parts][end],
                        dp[parts - 1][start] + cost[start][end]
                    )

        return dp[k][n]
