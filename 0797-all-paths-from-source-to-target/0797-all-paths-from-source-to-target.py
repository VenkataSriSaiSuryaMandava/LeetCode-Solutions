class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        cur = [0]

        def dfs(node):
            if node == len(graph) - 1:
                res.append(cur.copy())
                return

            for nei in graph[node]:
                cur.append(nei)
                dfs(nei)
                cur.pop()
        
        dfs(0)
        return res