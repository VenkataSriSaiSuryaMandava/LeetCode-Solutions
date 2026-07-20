class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(node, c):
            color[node] = c

            for nei in graph[node]:
                if color[nei] == c:
                    return False
                
                if color[nei] == 0:
                    if not dfs(nei, -c):
                        return False
            
            return True

        n = len(graph)
        color = [0 for i in range(n)]

        for i in range(n):
            if color[i] == 0:
                if not dfs(i, 1):
                    return False
        
        return True