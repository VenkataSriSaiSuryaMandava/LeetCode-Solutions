from typing import List
from collections import defaultdict

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = defaultdict(list)
        max_cost = -1
        
        for u, v, cost in edges:
            adj[u].append((v, cost))
            if cost > max_cost:
                max_cost = cost
                
        if max_cost == -1:
            return -1
            
        def check(mid: int) -> bool:
            dp = {}
            
            def dfs(u: int) -> float:
                if u == n - 1:
                    return 0
                if not online[u]:
                    return float('inf')
                if u in dp:
                    return dp[u]
                
                min_cost = float('inf')
                for v, cost in adj[u]:
                    if cost < mid:
                        continue
                    next_cost = dfs(v)
                    if next_cost != float('inf'):
                        min_cost = min(min_cost, cost + next_cost)
                        
                dp[u] = min_cost
                return min_cost

            return dfs(0) <= k

        low, high = 0, max_cost
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans