class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}

        def dfs(i, M, alice):
            if i == len(piles):
                return 0
            
            if (i, M, alice) in dp:
                return dp[(i, M, alice)]
            
            res = 0 if alice else float("inf")
            total = 0

            for X in range(1, 2 * M + 1):
                if i + X - 1 == len(piles):
                    break
                
                total += piles[i + X - 1]

                if alice:
                    res = max(res, total + dfs(i + X, max(M, X), not alice))
                else:
                    res = min(res, dfs(i + X, max(M, X), not alice))

            dp[(i, M, alice)] = res
            return res

        return dfs(0, 1, True) 