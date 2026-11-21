class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(s)
        adj = defaultdict(list)
        d = defaultdict(list)
        res = [0] * n
        
        for i in range(1, n):
            adj[parent[i]].append(i)
        
        def dfs(cur, parent):
            res[cur] = 1

            d[s[cur]].append(cur)

            for child in adj[cur]:
                dfs(child, cur)
            
            k = parent
            if len(d[s[cur]]) > 1:
                k = d[s[cur]][-2]
            
            if k != -1:
                res[k] += res[cur]
            
            d[s[cur]].pop()
        
        dfs(0, -1)
        return res