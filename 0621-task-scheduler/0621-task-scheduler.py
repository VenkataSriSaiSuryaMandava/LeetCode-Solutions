class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(int)
        for task in tasks:
            count[task] += 1
        
        maxheap = []
        for cnt in count.values():
            heapq.heappush(maxheap, -cnt)
        
        queue = deque()
        time = 0
        while maxheap or queue:
            time += 1
            if maxheap:
                cnt = 1 + heapq.heappop(maxheap)
                if cnt:
                    queue.append([cnt, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(maxheap, queue.popleft()[0])
        return time