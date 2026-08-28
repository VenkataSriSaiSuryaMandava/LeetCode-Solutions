class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])
        
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            
            queue = deque([[src, 1]])
            visited = set([src])

            while queue:
                n, w = queue.popleft()

                if n == target:
                    return w
                
                for nei, weight in adj[n]:
                    if nei not in visited:
                        queue.append([nei, w * weight])
                        visited.add(nei)
            
            return -1
        
        res = []

        for a, b in queries:
            res.append(bfs(a, b))
        
        return res