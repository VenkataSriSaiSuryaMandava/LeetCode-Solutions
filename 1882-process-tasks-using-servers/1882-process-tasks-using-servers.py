import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n = len(servers)
        m = len(tasks)
        
        free_servers = [(servers[i], i) for i in range(n)]
        heapq.heapify(free_servers)
        
        busy_servers = []
        ans = [0] * m
        curr_time = 0
        
        for j in range(m):
            curr_time = max(curr_time, j)
            
            if not free_servers:
                curr_time = busy_servers[0][0]
                
            while busy_servers and busy_servers[0][0] <= curr_time:
                finish_time, weight, idx = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, idx))
                
            weight, idx = heapq.heappop(free_servers)
            ans[j] = idx
            heapq.heappush(busy_servers, (curr_time + tasks[j], weight, idx))
            
        return ans