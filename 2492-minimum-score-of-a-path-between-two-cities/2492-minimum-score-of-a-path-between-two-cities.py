class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)

        for src, dst, dist in roads:
            adj[src].append([dst, dist])
            adj[dst].append([src, dist])
        
        self.res = float("inf")
        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for nei, dist in adj[node]:
                self.res = min(self.res, dist)
                dfs(nei)
        
        dfs(1)

        return self.res