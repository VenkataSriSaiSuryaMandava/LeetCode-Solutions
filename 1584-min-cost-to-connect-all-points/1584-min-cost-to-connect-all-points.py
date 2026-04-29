class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        adj = defaultdict(list)

        for i in range(n):
            xi, yi = points[i]

            for j in range(i + 1, n):
                xj, yj = points[j]

                dist = abs(xi - xj) + abs(yi - yj)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        minHeap = [[0, 0]]
        visit = set()
        res = 0

        while len(visit) < n:
            cost, point = heapq.heappop(minHeap)

            if point in visit:
                continue
            
            res += cost
            visit.add(point)

            for neiCost, nei in adj[point]:
                heapq.heappush(minHeap, [neiCost, nei])
        
        return res