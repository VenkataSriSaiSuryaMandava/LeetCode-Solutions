class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_p = 0
        if not prices or len(prices) == 1:  return 0
        cur_price = prices[0]
        for i in range(1, len(prices)):
            cur_price = min(cur_price, prices[i])
            max_p = max(max_p, prices[i] - cur_price)
        return max_p
        