class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        degree = [0] * len(graph)

        for i, nei in enumerate(graph):
            for node in graph[i]:
                adj[node].append(i)
            degree[i] = len(nei)

        queue = deque([node for node, deg in enumerate(degree) if deg == 0])

        while queue:
            node = queue.popleft()

            for nei in adj[node]:
                degree[nei] -= 1

                if degree[nei] == 0:
                    queue.append(nei)

        return [node for node, deg in enumerate(degree) if deg == 0]