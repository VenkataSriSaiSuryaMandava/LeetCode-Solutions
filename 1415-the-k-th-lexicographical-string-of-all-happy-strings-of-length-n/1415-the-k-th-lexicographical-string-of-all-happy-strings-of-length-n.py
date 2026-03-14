class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        
        def dfs(cur):
            if len(cur) == n:
                res.append(cur)
                return
            
            if len(res) == k:
                return 
            
            for ch in "abc":
                if not cur or cur[-1] != ch:
                    dfs(cur + ch)
        
        dfs("")

        if len(res) < k:
            return ""
        else:
            return res[k - 1]