class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        res = 0

        for src, dst in roads:
            graph[src].add(dst)
            graph[dst].add(src)
        
        for src in range(n):
            for dst in range(src + 1, n):
                rank = len(graph[src]) + len(graph[dst])

                if src in graph[dst]:
                    rank -= 1

                res = max(res, rank)
        
        return res