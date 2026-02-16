class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float("inf")] * len(days)
        dp.append(0)

        for i in range(len(days) - 1, -1, -1):
            j = i
            for cost, duration in zip(costs, [1, 7, 30]):
                while j < len(days) and days[j] < duration + days[i]:
                    j += 1
                dp[i] = min(dp[i], cost + dp[j])
        
        return dp[0]