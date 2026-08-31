class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)

        for i in range(n):
            xi, yi = points[i]

            for j in range(i + 1, n):
                xj, yj = points[j]
                
                dist = abs(xi - xj) + abs(yi - yj)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0
        visited = set()
        minHeap = [[0, 0]]

        while len(visited) < n:
            cost, point = heapq.heappop(minHeap)

            if point in visited:
                continue
            
            visited.add(point)
            res += cost

            for neiCost, nei in adj[point]:
                heapq.heappush(minHeap, [neiCost, nei])
        
        return res