class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        valToInd = defaultdict(list)
        for i, n in enumerate(arr):
            valToInd[n].append(i)
        
        queue = deque([0])
        visited = {0}
        res = 0

        while queue:
            for i in range(len(queue)):
                idx = queue.popleft()

                if idx == len(arr) - 1:
                    return res
                
                for j in (idx + 1, idx - 1, *valToInd.pop(arr[idx], [])):
                    if 0 <= j < len(arr) and j not in visited:
                        visited.add(j)
                        queue.append(j)
            
            res += 1