class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(set)
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)
        
        res = 0

        for a in range(n):
            for b in range(a + 1, n):
                cur = len(graph[a]) + len(graph[b])

                if a in graph[b]:
                    cur -= 1
                
                res = max(res, cur)
        
        return res