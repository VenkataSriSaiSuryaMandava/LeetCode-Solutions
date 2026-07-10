class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr = sorted((val, i) for i, val in enumerate(nums))
        
        pos = [0] * n
        for i, (_, orig_idx) in enumerate(arr):
            pos[orig_idx] = i
            
        farthest = [0] * n
        r = 0
        for i in range(n):
            while r < n and arr[r][0] - arr[i][0] <= maxDiff:
                r += 1
            farthest[i] = r - 1
            
        LOG = 18
        st = [[0] * LOG for _ in range(n)]
        
        for i in range(n):
            st[i][0] = farthest[i]
            
        for j in range(1, LOG):
            for i in range(n):
                st[i][j] = st[st[i][j-1]][j-1]
                
        ans = []
        for u, v in queries:
            a, b = pos[u], pos[v]
            if a == b:
                ans.append(0)
                continue
            if a > b:
                a, b = b, a
                
            steps = 0
            for j in range(LOG - 1, -1, -1):
                if st[a][j] < b:
                    steps += (1 << j)
                    a = st[a][j]
                    
            if st[a][0] >= b:
                ans.append(steps + 1)
            else:
                ans.append(-1)
                
        return ans