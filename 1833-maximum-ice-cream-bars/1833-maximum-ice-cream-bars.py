class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0

        for cost in costs:
            coins -= cost

            if coins < 0:
                break
            
            res += 1
        
        return res