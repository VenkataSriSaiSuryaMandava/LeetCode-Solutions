class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        queue = deque([[1, 0]])
        visited = {1}
        maxDepth = 0

        while queue:
            node, depth = queue.popleft()
            maxDepth = max(maxDepth, depth)

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append([nei, depth + 1])
        
        return pow(2, maxDepth - 1, MOD)
