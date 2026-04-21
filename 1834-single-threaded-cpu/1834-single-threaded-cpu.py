class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        for i, task in enumerate(tasks):
            task.append(i)
        
        tasks.sort()
        i = 0
        time = tasks[0][0]

        res = []
        minHeap = []

        while minHeap or i < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1
            
            if not minHeap:
                time = tasks[i][0]
            else:
                proctime, index = heapq.heappop(minHeap)
                time += proctime
                res.append(index)
        
        return res