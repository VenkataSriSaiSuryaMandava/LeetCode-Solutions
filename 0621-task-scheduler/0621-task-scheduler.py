class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = defaultdict(int)
        for task in tasks:
            count[task] += 1
        
        maxHeap = []
        for cnt in count.values():
            heapq.heappush(maxHeap, -cnt)
        
        queue = deque()
        time = 0

        while queue or maxHeap:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                
                if cnt:
                    queue.append([time + n, cnt])
            
            if queue and queue[0][0] == time:
                heapq.heappush(maxHeap, queue.popleft()[1])
        
        return time