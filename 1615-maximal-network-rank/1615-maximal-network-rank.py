class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        count = [0] * n

        for src, dst in roads:
            count[src] += 1
            count[dst] += 1
        
        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                res = max(res, count[i] + count[j] - 1)
        
        return res
