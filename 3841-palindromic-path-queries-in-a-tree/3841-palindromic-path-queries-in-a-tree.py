class Solution:

    def palindromePath(
        self, n: int, edges: list[list[int]], s: str, queries: list[str]
    ) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = (n).bit_length() + 1
        up = [[0] * LOG for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        d0 = [0] * n
        timer = 0

        chars = [1 << (ord(c) - 97) for c in s]

        # Iterative DFS to avoid recursion depth issues
        parent = [-1] * n
        order = []
        stack = [0]
        visited = [False] * n
        visited[0] = True

        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    stack.append(v)

        for u in order:
            up[u][0] = parent[u] if parent[u] != -1 else 0
            for j in range(1, LOG):
                up[u][j] = up[up[u][j - 1]][j - 1]
            p = parent[u]
            d0[u] = (d0[p] if p != -1 else 0) ^ chars[u]

        size = [1] * n
        for u in reversed(order):
            if parent[u] != -1:
                size[parent[u]] += size[u]

        time_counter = 1
        pos = [0] * n
        dfs_time_stack = [(0, False)]
        ptr = [0] * n

        timer = 1
        st = [0]
        index_in_adj = [0] * n
        tin[0] = 1

        while st:
            u = st[-1]
            if index_in_adj[u] < len(adj[u]):
                v = adj[u][index_in_adj[u]]
                index_in_adj[u] += 1
                if v != parent[u]:
                    timer += 1
                    tin[v] = timer
                    st.append(v)
            else:
                tout[u] = timer
                st.pop()

        def get_lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            return up[u][0]

        bit = [0] * (n + 2)

        def bit_update(idx: int, val: int):
            while idx <= n:
                bit[idx] ^= val
                idx += idx & (-idx)

        def bit_query(idx: int) -> int:
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_mask = 1 << (ord(parts[2]) - 97)
                diff = chars[u] ^ new_mask
                chars[u] = new_mask

                bit_update(tin[u], diff)
                bit_update(tout[u] + 1, diff)
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)

                du = d0[u] ^ bit_query(tin[u])
                dv = d0[v] ^ bit_query(tin[v])
                path_mask = du ^ dv ^ chars[lca]

                ans.append((path_mask & (path_mask - 1)) == 0)

        return ans