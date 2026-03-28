class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        res = [""] * n

        cur = 0
        for ch in ascii_lowercase:
            while cur < n and res[cur]:
                cur += 1
            
            if cur == n:
                break
            
            for j in range(cur, n):
                if lcp[cur][j] > 0:
                    res[j] = ch
        
        if "" in res:
            return ""

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if res[i] == res[j]:
                    if i == n - 1 or j == n - 1:
                        if lcp[i][j] != 1:
                            return ""
                    else:
                        if lcp[i][j] != lcp[i + 1][j + 1] + 1:
                            return ""
                else:
                    if lcp[i][j] != 0:
                        return ""
        
        return "".join(res)