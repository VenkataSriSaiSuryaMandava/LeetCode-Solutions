class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        for i, price in enumerate(prices):
            while stack and stack[-1][1] >= price:
                index, prev_price = stack.pop()
                prices[index] -= price
            
            stack.append([i, price])

        return prices