class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        max_factor = n

        freq = [0] * (max_factor + 1)
        for f, p in items:
            freq[f] += 1

        divisible_counts = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            for multiple in range(f, max_factor + 1, f):
                divisible_counts[f] += freq[multiple]

        offers = []
        min_price = min(p for f, p in items)

        for f, p in items:
            free_capacity = divisible_counts[f] - 1
            if free_capacity > 0 and p < 2 * min_price:
                offers.append((p, free_capacity))

        offers.sort()

        spent = 0
        answer = budget // min_price
        bonus_used = 0

        for price, cap in offers:
            if spent >= budget:
                break

            can_buy = min(cap, (budget - spent) // price)

            if can_buy == 0:
                continue
                
            spent += can_buy * price
            bonus_used += can_buy

            current = 2 * bonus_used + (budget - spent) // min_price
            answer = max(answer, current)

        return answer