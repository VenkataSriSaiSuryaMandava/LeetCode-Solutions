class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        f = [[] for i in range(n)]
        g = [[] for i in range(n)]

        suspicious = [False for i in range(n)]
        visited = [False for i in range(n)]

        for a, b in invocations:
            f[a].append(b)
            f[b].append(a)
            g[a].append(b)
        
        def dfs(i):
            suspicious[i] = True

            for j in g[i]:
                if not suspicious[j]:
                    dfs(j)
        
        dfs(k)

        def dfs2(i):
            visited[i] = True

            for j in f[i]:
                if not visited[j]:
                    suspicious[j] = False
                    dfs2(j)

        for i in range(n):
            if not visited[i] and not suspicious[i]:
                dfs2(i)
        
        return [i for i in range(n) if not suspicious[i]]