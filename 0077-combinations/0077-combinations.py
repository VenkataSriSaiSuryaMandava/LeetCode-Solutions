class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        cur = []

        def backtrack(i):
            if len(cur) == k:
                res.append(cur.copy())
                return
            
            if i > n:
                return 
            
            cur.append(i)
            backtrack(i + 1)

            cur.pop()
            backtrack(i + 1)
        
        backtrack(1)

        return res