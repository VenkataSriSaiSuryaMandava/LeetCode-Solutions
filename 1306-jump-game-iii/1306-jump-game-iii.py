class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        queue = deque([(start)])
        visited = set()

        while queue:
            i = queue.popleft()

            if arr[i] == 0:
                return True
            
            if i in visited:
                continue
            
            visited.add(i)

            left = i - arr[i]
            right = i + arr[i]

            if 0 <= left < n:
                queue.append(left)
            
            if 0 <= right < n:
                queue.append(right)
        
        return False