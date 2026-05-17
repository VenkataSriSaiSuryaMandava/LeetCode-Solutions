from collections import deque

class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        
        n = len(arr)
        visited = set()
        q = deque([start])

        while q:
            i = q.popleft()

            if arr[i] == 0:
                return True

            if i in visited:
                continue

            visited.add(i)

            left = i - arr[i]
            right = i + arr[i]

            if 0 <= left < n:
                q.append(left)

            if 0 <= right < n:
                q.append(right)

        return False