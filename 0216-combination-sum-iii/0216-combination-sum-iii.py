class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(k, n, start):
            if k == 0 and n == 0:
                res.append(cur.copy())
                return
            
            if k <= 0:
                return
            
            for i in range(start, min(10, n + 1)):
                cur.append(i)
                dfs(k - 1, n - i, i + 1)
                cur.pop()
        
        dfs(k, n, 1)

        return res
