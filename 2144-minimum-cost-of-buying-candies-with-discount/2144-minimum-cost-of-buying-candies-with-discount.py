class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost = reversed(sorted(cost))
        res = 0

        for i, c in enumerate(cost):
            if (i + 1) % 3:
                res += c
        
        return res