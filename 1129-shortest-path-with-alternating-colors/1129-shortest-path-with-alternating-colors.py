class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [defaultdict(list), defaultdict(list)]

        for node, nei in redEdges:
            graph[0][node].append(nei)
        
        for node, nei in blueEdges:
            graph[1][node].append(nei)
        
        res = [-1] * n
        queue = deque([(0, 0), (0, 1)])
        visited = set()
        distance = 0

        while queue:
            for i in range(len(queue)):
                node, color = queue.popleft()
                visited.add((node, color))

                if res[node] == -1:
                    res[node] = distance
                
                color ^= 1

                for nei in graph[color][node]:
                    if (nei, color) not in visited:
                        queue.append((nei, color))

            distance += 1
        
        return res