class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        queue = deque()
        edges_count = {}

        for src, nei in adj.items():
            if len(nei) == 1:
                queue.append(src)
            
            edges_count[src] = len(nei)
        
        while queue:
            if n <= 2:
                return list(queue)
            
            for i in range(len(queue)):
                node = queue.popleft()
                n -= 1

                for nei in adj[node]:
                    edges_count[nei] -= 1

                    if edges_count[nei] == 1:
                        queue.append(nei)