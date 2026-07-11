from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * n
        complete_components_count = 0
        
        def dfs(node: int, component_nodes: list):
            visited[node] = True
            component_nodes.append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component_nodes)
        
        for i in range(n):
            if not visited[i]:
                component_nodes = []
                dfs(i, component_nodes)
                
                m = len(component_nodes)
                total_degree = sum(len(adj[vertex]) for vertex in component_nodes)
                
                if total_degree == m * (m - 1):
                    complete_components_count += 1
                    
        return complete_components_count