class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        stoneSum = sum(stones)
        target = ceil(stoneSum / 2)
        dp = {}

        def dfs(i, total):
            if (i, total) in dp:
                return dp[(i, total)]
            
            if i == len(stones) or total >= target:
                return abs(total - (stoneSum - total))
            
            dp[(i, total)] = min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))

            return dp[(i, total)]
        
        return dfs(0, 0)