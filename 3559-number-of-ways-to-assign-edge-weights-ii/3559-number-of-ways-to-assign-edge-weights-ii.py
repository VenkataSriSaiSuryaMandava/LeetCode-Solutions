class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        n = len(edges) + 1

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = (n + 1).bit_length()

        depth = [0] * (n + 1)
        parent = [[0] * (n + 1) for _ in range(LOG)]

        q = deque([1])
        visited = {1}

        while q:
            node = q.popleft()

            for nei in graph[node]:
                if nei in visited:
                    continue

                visited.add(nei)
                depth[nei] = depth[node] + 1
                parent[0][nei] = node
                q.append(nei)

        for j in range(1, LOG):
            for i in range(1, n + 1):
                parent[j][i] = parent[j - 1][parent[j - 1][i]]

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a

            diff = depth[a] - depth[b]

            for j in range(LOG):
                if diff & (1 << j):
                    a = parent[j][a]

            if a == b:
                return a

            for j in range(LOG - 1, -1, -1):
                if parent[j][a] != parent[j][b]:
                    a = parent[j][a]
                    b = parent[j][b]

            return parent[0][a]

        ans = []

        for u, v in queries:
            p = lca(u, v)

            k = depth[u] + depth[v] - 2 * depth[p]

            if k == 0:
                ans.append(0)
            else:
                ans.append(pow(2, k - 1, MOD))

        return ans