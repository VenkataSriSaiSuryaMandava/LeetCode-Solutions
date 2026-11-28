class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        bonus_count = []
        for i in range(n):
            count = 1

            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    count += 1
            bonus_count.append(count)

        dp = [0] * (budget + 1)

        for i in range(n):
            factor, price = items[i]
            bonus = bonus_count[i]
            new_dp = dp[ : ]

            for w in range(price, budget + 1):
                if dp[w - price] + bonus > new_dp[w]:
                    new_dp[w] = dp[w - price] + bonus

            for w in range(price, budget + 1):
                if new_dp[w - price] + 1 > new_dp[w]:
                    new_dp[w] = new_dp[w - price] + 1

            dp = new_dp

        return dp[budget]