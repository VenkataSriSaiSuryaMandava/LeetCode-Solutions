class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [0] * n

        if k > n:
            res = 0
            for i in range(1, n):
                profit = prices[i] - prices[i - 1]

                if profit > 0:
                    res += profit

            return res
        
        for t in range(k):
            pos = -prices[0]
            profit = 0

            for i in range(1, n):
                pos = max(pos, dp[i] - prices[i])
                profit = max(profit, pos + prices[i])
                dp[i] = profit
        
        return dp[-1]