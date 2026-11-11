class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        common = min(need1, need2)
        
        rem1 = need1 - common
        rem2 = need2 - common

        total = common * min(cost1 + cost2, costBoth)

        total += rem1 * min(costBoth, cost1)
        total += rem2 * min(costBoth, cost2)

        return total