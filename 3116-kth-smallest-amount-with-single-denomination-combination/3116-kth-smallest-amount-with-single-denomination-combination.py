class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        subsets = []
        for mask in range(1, 1 << n):
            lcm_val = 1
            for i in range(n):
                if (mask >> i) & 1:
                    lcm_val = math.lcm(lcm_val, coins[i])
            sign = 1 if bin(mask).count('1') % 2 == 1 else -1
            subsets.append((lcm_val, sign))
        
        def count(x: int) -> int:
            return sum(sign * (x // lcm_val) for lcm_val, sign in subsets)

        low, high = 1, min(coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans