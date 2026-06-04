class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float("inf")] * (len(days) + 1)
        dp[-1] = 0

        for i in range(len(days) - 1, -1, -1):
            j = i

            for cost, duration in zip(costs, [1, 7, 30]):
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1
                
                dp[i] = min(dp[i], dp[j] + cost)
        
        return dp[0]