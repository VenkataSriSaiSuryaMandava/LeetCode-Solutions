class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        queue = deque()
        edgesCount = {}

        for src, nei in adj.items():
            if len(nei) == 1:
                queue.append(src)
            
            edgesCount[src] = len(nei)
        
        while queue:
            if n <= 2:
                return list(queue)

            for i in range(len(queue)):
                n -= 1
                node = queue.popleft()

                for nei in adj[node]:
                    edgesCount[nei] -= 1

                    if edgesCount[nei] == 1:
                        queue.append(nei)